from django.contrib import admin

from .models import MeterType, SerialBus, Remote, Meter

# Register your models here.

admin.site.register(MeterType)
admin.site.register(SerialBus)
admin.site.register(Remote)
admin.site.register(Meter)