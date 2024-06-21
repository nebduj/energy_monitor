from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from meter_table_updater import process_data 

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_data.process_updates, 'interval', minutes=1)
    scheduler.start()