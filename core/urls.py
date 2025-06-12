from django.urls import path
from core import views

urlpatterns = [
    path("public/", views.public_view),
    path("protected/", views.protected_view),
    path("register/", views.register_user),
]