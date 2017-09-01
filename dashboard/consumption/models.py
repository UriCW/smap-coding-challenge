# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    user_id=models.IntegerField(unique=True); #TODO index by this
    user_area=models.CharField(max_length=2);
    user_tariff=models.CharField(max_length=2);

class Consumption(models.Model):
    user=models.ForeignKey(User);
    consumption_time=models.DateTimeField();
    consumption_amount=models.DecimalField(decimal_places=2,max_digits=20);
