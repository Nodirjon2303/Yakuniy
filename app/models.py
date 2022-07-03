from django.db import models

class Fanlar(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.name}"


class Baza(models.Model):
    fan = models.ForeignKey(Fanlar, models.CASCADE)
    baza = models.FileField(upload_to='baza savollar')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.fan.name}"

