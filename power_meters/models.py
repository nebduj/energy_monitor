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
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
class SecondMeasurements(models.Model):
    meter = models.ForeignKey(Meter,models.CASCADE)
    rms = models.FloatField("RMS Value")
    whr = models.FloatField("Watt Hour")
    raw_peak = models.IntegerField("Highest Raw Value")
    raw_min = models.IntegerField("Lowest Raw Value")
    aggregated = models.BooleanField("Data has been aggregated", default = "False")

class MinuteMeasurements(models.Model):
    meter = models.ForeignKey(Meter,models.CASCADE)
    rms = models.FloatField("Average RMS Value")
    whr = models.FloatField("Watt Hour")
    aggregated = models.BooleanField("Data has been aggregated", default = "False")
    
class HourlyMeasurements(models.Model):
    meter = models.ForeignKey(Meter,models.CASCADE)
    rms = models.FloatField("Average RMS Value")
    whr = models.FloatField("Watt Hour")
    peak_rms = models.FloatField("Highest RMS Value")
    aggregated = models.BooleanField("Data has been aggregated", default = "False")
    

class DailyMeasurements(models.Model):
    meter = models.ForeignKey(Meter,models.CASCADE)
    rms = models.FloatField("Average RMS Value")
    whr = models.FloatField("Watt Hour")
    peak_hr = models.IntegerField("Peak Demand Hour")
    peak_hr_usage = models.FloatField("Wh Usage at Peak Hour")
    peak_rms = models.FloatField("Highest RMS Value")
    peak_demand_period = models.IntegerField("Peak Demand Period")
    peak_demand_usage = models.FloatField("Wh Usage at Peak Period")
    aggregated = models.BooleanField("Data has been aggregated", default = "False")
    
class MonthlyMeasurements(models.Model):
    meter = models.ForeignKey(Meter,models.CASCADE)
    rms = models.FloatField("Average RMS Value")
    whr = models.FloatField("Watt Hour")
    peak_day = models.IntegerField("Peak Demand Hour")
    peak_day_usage = models.FloatField("Wh Usage at Peak Hour")
    peak_rms = models.FloatField("Highest RMS Value")
    peak_demand_period = models.IntegerField("Peak Demand Period")
    peak_demand_usage = models.FloatField("Wh Usage at Peak Period")
    
        
    
    
