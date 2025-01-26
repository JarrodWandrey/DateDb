from django.db import models
import datetime

# Create your models here.
class Date(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(default=datetime.date.today)