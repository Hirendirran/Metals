from django.db import models

class MetalPrice(models.Model):
    date = models.DateField(unique=True)
    gold = models.FloatField()
    silver = models.FloatField()
    platinum = models.FloatField()
    diamond = models.FloatField()

    def __str__(self):
        return str(self.date)
