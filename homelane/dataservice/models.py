from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateTimeField()
    price = models.FloatField()
    bedrooms = models.FloatField()
    bathrooms = models.FloatField()
    sqft_living = models.FloatField()
    sqft_lot = models.FloatField()
    floors = models.FloatField()
    waterfront = models.IntegerField()
    view = models.IntegerField()
    condition = models.IntegerField()
    sqft_above = models.FloatField()
    sqft_basement = models.FloatField()
    yr_built = models.IntegerField()
    yr_renovated = models.IntegerField()
    street = models.TextField()
    city = models.TextField()
    statezip = models.TextField()
    country = models.TextField()