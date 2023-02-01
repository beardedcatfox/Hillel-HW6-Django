from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=119)
    last_name = models.CharField(max_length=119)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
