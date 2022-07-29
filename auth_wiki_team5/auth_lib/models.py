from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.full_name
