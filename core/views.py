from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.tasks import send_welcome_email

@api_view(["GET"])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint."})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "This is a protected endpoint only for logged in users."})

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken."}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    send_welcome_email.delay(username, email)
    return Response({"message": "User registered successfully. Email will be sent in background."})