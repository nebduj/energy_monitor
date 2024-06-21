from power_meters.models import Meter, MinuteMeasurements, SecondMeasurements
from datetime import datetime
from django.utils import timezone

def process_updates():
        update_minutes();
        

def update_minutes(end_time):
        for current_meter in Meter.objects.filter(active):
            now = timezone.now()
            new_data = SecondMeasurements.objects.filter(aggregated = False, meter = current_meter)
            
            #latest = SecondMeasurements
            pass

