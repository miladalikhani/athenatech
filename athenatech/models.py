from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.username