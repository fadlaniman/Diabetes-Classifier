from django.contrib import admin
from polls.models import Diabetes

class DiabetesAdmin(admin.ModelAdmin):
    list_display = ['id','pregnancies','glucose','bloodPressure','skinThickness','insulin','bmi','diabetesPedigreeFunction','age','outcome']

admin.site.register(Diabetes, DiabetesAdmin)