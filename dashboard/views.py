from .serializers import HealthCheckSerializer
from .models import HealthCheck
from django.http import HttpResponse
from rest_framework import generics
import requests
from datetime import datetime 
from django.shortcuts import get_object_or_404
from .utils import statusMail

class SiteCreateAPIView(generics.ListCreateAPIView):
    serializer_class=HealthCheckSerializer
    queryset=HealthCheck.objects.all()
    
    
def check_system():

    queryset=HealthCheck.objects.values('id')
    for d in queryset:
        site=HealthCheck.objects.get(id=d['id'])
        url=site.site_url
        resp=requests.get(url)
        status=resp.status_code
        site.site_status=status
        time=datetime.now()
        site.last_check_at=time
        data={
            "to_email":site.email
              }
        if status is not 200:
            statusMail(data)
        site.save()
    return HttpResponse("Serverless Cronjob")
    
