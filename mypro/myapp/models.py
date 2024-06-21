from django.db import models

class FORM(models.Model):
    name=models.CharField(max_length=100)
    reg_no=models.IntegerField()
    Dept=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
