from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} joined on {self.date_joined}'


class Desc(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} posted at {self.date}'
