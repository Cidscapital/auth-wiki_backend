from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    years_of_programming_experience = models.PositiveIntegerField(null=True, blank=True)