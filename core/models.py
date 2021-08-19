from django.db import models
import datetime

# Create your models here.

class Message(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField(max_length=100)
    subject = models.CharField(max_length= 100)
    message = models.TextField()
    date    = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name + " " + self.email

    class Meta:
        verbose_name_plural = 'Messages'
        db_table = 'Messages'