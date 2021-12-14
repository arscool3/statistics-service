from django.db import models

class Statistic(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(blank=True, max_digits=100, decimal_places=2, null=True)
    cpc = models.DecimalField(blank=True, max_digits=100, decimal_places=2, null=True)
    cpm = models.DecimalField(blank=True, max_digits=100, decimal_places=2, null=True)