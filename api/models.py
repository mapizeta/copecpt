from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
import uuid as uuid_lib

class User(AbstractUser):
    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD  = "email"
    username        = None
    email           = models.EmailField("email address", blank=False, null=False, unique=True)
    id              = models.UUIDField(default=uuid_lib.uuid4,unique=True,primary_key=True,editable=False)
    fecha_nac       = models.DateField(blank=True, null=True)
    nombre          = models.CharField(max_length=50,blank=True, null=True)
    apellido        = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return self.email