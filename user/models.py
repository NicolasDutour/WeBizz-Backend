from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class User(AbstractUser):
    address = models.CharField('Adresse', max_length=150, null=True, blank=True)
    postal_code = models.CharField('Code Postal', max_length=15)
    city = models.CharField('Ville', max_length=150)
    country = CountryField('Pays')
    phone_number = models.CharField('Téléphone', max_length=150)
    birthday = models.DateField('Date de naissance')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = 'Client'
