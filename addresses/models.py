import geocoder
from django.db import models



mapbox_access_token = 'pk.eyJ1IjoiYWxpZHVnIiwiYSI6ImNsZGpoanZuazAwaHczcXFrMzBjZnZpbDcifQ.Pk65OCZgC5O4Zq4f7YI86g'

# Create your models here.
class Address(models.Model):
    '''
    Hi! This class turns an address into a Lat,Long
    '''
    address=models.TextField()
    #user can input an address with lat,long coords 
    #to convert in mapbox API ansd display it on the map
    lat=models.FloatField(blank=True, null=True)
    #blank is ok, initially store as none
    long=models.FloatField(blank=True, null=True)
    
    #use python geocoder:
    #docs here: https://geocoder.readthedocs.io/providers/Mapbox.html
    
    #make sure you've done pip install geocoder
    
    def save(self,*args, **kwargs):
        'make the API call here'
        g = geocoder.mapbox(self.address, key = mapbox_access_token)
        g=g.latlng # returns [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs )
    