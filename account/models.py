from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_sender = models.BooleanField(verbose_name='Продавец/Покупатель')

    def __str__(self):
        return self.user.username
