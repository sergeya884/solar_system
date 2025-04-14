from django.contrib import admin
from .models import CelestialBody

@admin.register(CelestialBody)
class CelestialBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_planet')
    search_fields = ('name',)
