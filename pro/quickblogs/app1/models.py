from django.db import models
class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, default='dp.png')
    def __str__(self):
        return self.username

class posts(models.Model):
    username = models.CharField(max_length=50)
    image = models.FileField()
    title = models.CharField(max_length=500)
    content = models.TextField()
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.username


# Create your models here.
