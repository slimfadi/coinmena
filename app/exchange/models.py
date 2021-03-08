from django.db import models

class BtcPrice(models.Model):

    time = models.DateTimeField(auto_now_add=True)

    price = models.FloatField()