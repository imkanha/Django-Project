from django.db import models

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length = 200)
    item_decs = models.CharField(max_length = 200)
    item_price = models.IntegerField(default=0)