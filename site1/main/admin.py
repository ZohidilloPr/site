from django.contrib import admin
from .models import (
    DistrictAndCity,
    Foreign_language,
    Neighborhood,
    College,
    School,
    University,
    Interest,
    Opportunity,
    Students,
)
# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["f_name", "districtandcity", "neighborhood"]

admin.site.register(DistrictAndCity)
admin.site.register(Foreign_language)
admin.site.register(Neighborhood)
admin.site.register(College)
admin.site.register(School)
admin.site.register(University)
admin.site.register(Interest)
admin.site.register(Opportunity)