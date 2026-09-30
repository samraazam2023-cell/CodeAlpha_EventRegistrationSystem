from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def register_event(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
def registration_list(request):
    registrations = Registration.objects.all()
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def cancel_registration(request, registration_id):
    try:
        registration = Registration.objects.get(id=registration_id)
    except Registration.DoesNotExist:
        return Response({"error": "Registration not found"}, status=404)

    registration.delete()
    return Response({"message": "Registration cancelled successfully"})