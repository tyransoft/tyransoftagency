from django.db import models

# Create your models here.
class myinfo(models.Model):
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return self.email
        
