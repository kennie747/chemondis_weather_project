from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=200)
    # country = models.CharField(max_length=200)
    # temperature = models.IntegerField()
    # min_temp = models.IntegerField()
    # max_temp = models.IntegerField()
    # humidity = models.IntegerField()
    # pressure = models.IntegerField()
    # wind_speed = models.IntegerField()
    # wind_direction = models.IntegerField()
    # description=models.CharField(max_length=200)

    # def __str__(self):
    #     return f'{self.title} from {self.year}' 
