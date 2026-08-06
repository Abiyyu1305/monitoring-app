from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nama_lengkap = models.CharField(max_length=100)

    no_hp = models.CharField(max_length=20)

    divisi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_lengkap
