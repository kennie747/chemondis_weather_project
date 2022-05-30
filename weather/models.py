from django.db import models

class Weather(models.Model):
    city_name=models.CharField(max_length=200)
    longitude=models.IntegerField()

    def __str__(self):
        return f'{self.title} from {self.year}' 
