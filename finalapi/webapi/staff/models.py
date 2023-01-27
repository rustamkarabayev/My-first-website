from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo/staff")


class Services(models.Model):
    name = models.CharField(max_length=100, verbose_name="название сервиса")
    title = models.CharField(max_length=100, verbose_name="описание сервиса")

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
