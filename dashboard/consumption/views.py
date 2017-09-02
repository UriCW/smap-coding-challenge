# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import User,Consumption
from django.db.models import Sum, Max, Min, Avg


def summary(request):
    all_users=User.objects.all();
    #time_chart_data=Consumption.objects.values('consumption_time').annotate( total=Sum('consumption_amount'), average=Avg('consumption_amount') ).order_by('consumption_time')
    time_chart_data=Consumption.objects.extra(select={'day': 'date(consumption_time)'}).values('day').annotate( maximum=Max('consumption_amount'), average=Avg('consumption_amount') ).order_by('consumption_time')#TODO check this yelds the correct results


    context = {
        'message': 'Hello!',
        'users'  : all_users,
        'time_chart' : time_chart_data,
    }
    return render(request, 'consumption/summary.html', context)

def detail(request,UID):
    user=User.objects.filter(user_id=UID)
    consumption=Consumption.objects.filter(user=user)
    context = {
        'uid':UID,
        'consumption':consumption,
    }
    return render(request, 'consumption/detail.html', context)
