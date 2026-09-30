from rest_framework import serializers
from .models import Event, Registration


class EventSerializer(serializers.ModelSerializer):
    registered_count = serializers.SerializerMethodField()
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'location',
            'capacity',
            'registered_count',
            'available_seats'
        ]

    def get_registered_count(self, obj):
        return Registration.objects.filter(event=obj).count()

    def get_available_seats(self, obj):
        registered = Registration.objects.filter(event=obj).count()
        return max(obj.capacity - registered, 0)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'registered_at']

    def validate(self, data):
        user = data.get('user')
        event = data.get('event')

        if Registration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError(
                "This user is already registered for this event."
            )

        registration_count = Registration.objects.filter(event=event).count()

        if registration_count >= event.capacity:
            raise serializers.ValidationError(
                "This event is full."
            )

        return data