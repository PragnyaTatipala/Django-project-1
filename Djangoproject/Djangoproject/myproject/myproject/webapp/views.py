from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import timediff
from . serializers import timediffSerializer
from datetime import date
from datetime import datetime
from django.http import Http404
from django.http import JsonResponse
import json


## Calcutate the timediff from the url requests and returns Json response
def sec_results_date(request, start_year, start_month, start_day,  end_year, end_month, end_day):
        
        start_time = date(start_year, start_month, start_day)
        end_time = date(end_year, end_month, end_day)

        if(end_time < start_time):
          #response = "Invalid end time - start time conditions"
          raise Http404("Invalid end time - start time conditions")
          #return HttpResponse(response)
        else:
          time_diff = end_time - start_time
          seconds = time_diff.total_seconds()
          #response = "Time differenc in Seconds %f."
          sec_dict = { 'start_time': start_time,
                     'end_time': end_time,
                     'Time difference in Seconds': seconds}
          #json_object = json.dumps(sec_dict,indent=1)
          return JsonResponse(sec_dict)
          #return HttpResponse(response % seconds)

## Calcutate the timediff from the url requests and returns Json response
def sec_results(request, start_year, start_month, start_day, start_hour, start_min, start_sec, end_year, end_month, end_day, end_hour, end_min, end_sec):
        
        start_time = datetime(start_year, start_month, start_day,start_hour, start_min, start_sec)
        end_time = datetime(end_year, end_month, end_day, end_hour, end_min, end_sec)

        if(end_time < start_time):
          response = "Invalid end time - start time conditions"
          raise Http404("Invalid end time - start time conditions")
          #return HttpResponse(response)
        else:
          time_diff = end_time - start_time
          seconds = time_diff.total_seconds()
          response = "Time differenc in Seconds %f."
          sec_dict = { 'start_time': start_time,
                     'end_time': end_time,
                     'Time difference in Seconds': seconds}
          #json_object = json.dumps(sec_dict,indent=1)
          return JsonResponse(sec_dict)

def index(request):
    response = "Index page"
    return HttpResponse(response)



class timediffout(APIView):
    ## Calcutate the timediff from the url requests and returns Json response
    def get(self, request):
        
        ## get an model object which has the start_time and end_time
        timediff_obj2 = timediff.objects.get()
        flag = timediff_obj2.calculate_timediff() ## function that calculates time_diff and returns valid or not as flag and seconds are updated in its class

        if(flag == 0):
            raise Http404("Invalid end time - start time conditions")
        else:
            #timediff_obj = timediff.objects.all()
            #serializer = timediffSerializer(timediff_obj, many= True) 
            sec_dict = { 'Time difference in Seconds': timediff_obj2.seconds,
                     'start_time': timediff_obj2.start_time,
                     'end_time': timediff_obj2.end_time}
           #json_object = json.dumps(sec_dict,indent=1)
            return JsonResponse(sec_dict)
            #return Response(serializer.data)

    def post(self):
        pass