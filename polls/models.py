from django.db import models

class Diabetes(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    bloodPressure = models.IntegerField()
    skinThickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.DecimalField(max_digits=3, decimal_places=1)
    diabetesPedigreeFunction = models.DecimalField(max_digits=4, decimal_places=3)
    age = models.IntegerField()
    outcome = models.IntegerField()
        






