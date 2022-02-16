from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    TIPO = (('parceiro', 'parceiro'), ('interno', 'interno'))

    type_user = models.CharField(choices=TIPO, max_length=255)
