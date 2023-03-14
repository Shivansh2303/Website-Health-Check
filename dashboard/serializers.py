from rest_framework import serializers
from rest_framework.response import Response

from urllib.request import urlopen
from django.core.validators import URLValidator
from django.utils import timezone
from bs4 import BeautifulSoup
import requests
import urllib3
from datetime import datetime 


from .models import HealthCheck
from .utils import statusMail

urllib3.disable_warnings()



class HealthCheckSerializer(serializers.ModelSerializer):
    site_name=serializers.CharField(read_only=True)
    site_url=serializers.CharField(required=True)
    site_status=serializers.IntegerField(default=404,allow_null=True,read_only=True)
    email=serializers.EmailField(required=True)
    last_check_at=serializers.DateTimeField(read_only=True)
    
    
    def validate_site_url(self, site_url):
        if '://'  not in site_url:
            site_url='http://'+site_url
        return site_url
    
    class Meta:
        model=HealthCheck
        fields=['id','site_name','site_url','email','site_status','last_check_at']
    
    def create(self, validated_data):
        status=404
        site_name=''
        email=validated_data['email']
        url=validated_data['site_url'] 
        resp=requests.get(url)
        url=resp.url
        time=datetime.now()
        try:
            status=resp.status_code
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                }
            html_page = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html_page, 'html.parser')
            site_name=soup.title.text
            print(site_name)
        except requests.exceptions.ConnectionError as e:
            return None
        except requests.exceptions.MissingSchema as e:
            return None
        except requests.exceptions.ConnectionError as e:
            return None
        return HealthCheck.objects.create(
            site_url=url,
            site_status=status,
            site_name=site_name ,
            email=email,
            last_check_at=time
        )


    

        
