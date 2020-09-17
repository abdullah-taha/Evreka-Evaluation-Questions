from django.shortcuts import render
from .models import *
from datetime import date, timedelta,datetime
from django.http.response import JsonResponse, HttpResponse

# views for question 1

def get_lst_points(request):
    """
    returns a list of last points per vehicle that have sent navigation data in the last 48 hours
    """
    points = []
    x = NavigationRecord.objects.select_related("vehicle").filter(datetime__gt = datetime.today()-timedelta(hours=48))
    for i in x:
        points.append({"latitude": i.latitude,
                        "longitude":i.longitude,  
                        "vehicle_plate":i.vehicle.plate,
                        "datetime":i.datetime})
    return JsonResponse(points, safe=False)




# views for question 2

def get_collection_freq(request):
    """
    returns a list of collection_frequency values for all Bin-Operation pairs
    """
    x = Collection.objects.values_list("collection_frequency", flat=True)
    return JsonResponse(list(x), safe=False)

