from django.db import models

# Create your models here.

class shift_rota(models.Model):
    location=models.CharField(max_length=50)
    application=models.CharField(max_length=50,null=True)
    Resource_Analyst=models.CharField(max_length=50,null=True)
    shift_date=models.DateField()
    shift=models.CharField(max_length=4)

    def __str__(self):
        return self.Resource_Analyst