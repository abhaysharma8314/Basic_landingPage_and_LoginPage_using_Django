from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122, null=True)
    suggestion=models.TextField(max_length=122, null=True)
    date=models.DateField()

    def __str__(self):
         return self.email
