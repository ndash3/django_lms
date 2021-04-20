from django.contrib import admin
from leave_mngt.models import shift_rota as sr
from import_export.admin import ImportExportModelAdmin as IEMA
# Register your models here.

class ShiftAdmin(IEMA,admin.ModelAdmin):
    list_display = ['location','application','Resource_Analyst','shift_date','shift']

admin.site.register(sr,ShiftAdmin)
