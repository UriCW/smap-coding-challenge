# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import User,Consumption
from django.db.models import Sum, Max, Min, Avg


def summary(request):
    all_users=User.objects.all();
    #time_chart_data=Consumption.objects.values('consumption_time').annotate( total=Sum('consumption_amount'), average=Avg('consumption_amount') ).order_by('consumption_time') #Retrives total consumption and average consumption by 30minutes slot.
    time_chart_data=Consumption.objects.extra(select={'day': 'date(consumption_time)'}).values('day').annotate( maximum=Max('consumption_amount'), average=Avg('consumption_amount') ).order_by('consumption_time')#Retrives total consumption and average consumption by day @TODO check this is correct
    #time_chart_data=Consumption.objects.extra({'day':"date(consumption_time)"}).values_list('day').annotate(Avg('consumption_amount'),Max('consumption_amount') )
    context = {
        'users'  : all_users,
        'time_chart' : time_chart_data,
    }#@TODO don't pass a queryset, format users and timechart and pass in array, then fix in template.
    return render(request, 'consumption/summary.html', context)

def detail(request,UID):
    user=User.objects.filter(user_id=UID)
    consumption=Consumption.objects.filter(user=user)
    context = {
        'uid':UID,
        'tariff': user[0].user_tariff,
        'area': user[0].user_area,
        'consumption':consumption,
    }
    return render(request, 'consumption/detail.html', context)
