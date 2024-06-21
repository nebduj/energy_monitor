from django.apps import AppConfig


class PowerMetersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'power_meters'
    
    def ready(self):
        from meter_table_updater import updater
        updater.start()
