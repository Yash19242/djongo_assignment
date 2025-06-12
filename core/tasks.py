from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(username, email):
    subject = "Welcome!"
    message = f"Hi {username}, thanks for registering!"
    from_email = "admin@example.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return f"Sent email to {email}"