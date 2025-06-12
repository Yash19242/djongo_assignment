from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.username