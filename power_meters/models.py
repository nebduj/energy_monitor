from email.policy import default
from django.db import models

# Create your models here.
class MeterType(models.Model):
    name = models.CharField(max_length=20, unique = True)
    
    def __str__(self):
        return self.name

class SerialBus(models.Model):
    name = models.CharField(max_length=20, unique = True)
    sck = models.IntegerField("SPI Clock Pin", unique = True) 
    mosi = models.IntegerField("Master Out, Slave In", unique = True) 
    miso = models.IntegerField("Master In, Slave Out", unique = True) 
    def __str__(self):
        return self.name

class Remote(models.Model):
    name = models.CharField(max_length=20, unique = True)
    chip_select = models.IntegerField("Chip Select Pin on Pi", unique = True)
    inputs = models.IntegerField("Number of Inputs on Remote", default=8)
    vdd = models.FloatField("VDD for remote", default=5.0)
    max_value = models.IntegerField("Maximum raw value", default=1024)
    serial_bus = models.ForeignKey(SerialBus, models.PROTECT)
    def __str__(self):
        return self.name
    
class Meter(models.Model):
    name = models.CharField(max_length=20, unique = True)
    input_number = models.IntegerField() 
    calibrated_zero = models.IntegerField(default=512)
    remote = models.ForeignKey(Remote, models.PROTECT)
    meter_type = models.ForeignKey(MeterType, models.PROTECT)
    associated_voltage_meter = models.ForeignKey('self', models.PROTECT,blank=True)
    ratio = models.FloatField(default=20)
    def __str__(self):
        return self.name

    
        
    
    
