from django.db import models

# Create your models here.
class service(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="images")
    desc1=models.CharField(max_length=100)
    desc2=models.TextField(max_length=500)

    def __str__(self):
        return self.name
class customer(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="images")
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.name