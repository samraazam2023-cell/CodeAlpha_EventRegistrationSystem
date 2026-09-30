# CodeAlpha Event Registration System

A simple Event Registration System built using Django and Django REST Framework.

## Features

- View all events
- View event details
- Register for an event
- View registrations
- Cancel a registration
- Admin panel for managing events and registrations
- SQLite database

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

GET /api/events/
View all events.

GET /api/events/1/
View details of a specific event.

POST /api/register/
Register a user for an event.

GET /api/registrations/
View all registrations.

DELETE /api/registrations/1/
Cancel a registration.

## How to Run

1. Install dependencies:

py -m pip install django djangorestframework

2. Run migrations:

py manage.py migrate

3. Start the server:

py manage.py runserver

4. Open:

http://127.0.0.1:8000/api/events/

## Admin Panel

http://127.0.0.1:8000/admin/