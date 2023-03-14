from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator


class OptionalSchemeURLValidator(URLValidator):
    def __call__(self,value):
        if '://' not in value:
            value='http://'+value
        super(OptionalSchemeURLValidator,self).__call__(value)


class HealthCheck(models.Model):
    site_name=models.CharField(max_length=255,null=False)
    site_url=models.URLField(max_length=25,blank=False,null=False,validators=[OptionalSchemeURLValidator])
    site_status=models.IntegerField(blank=False,default=404)
    email=models.EmailField(max_length=50,blank=False,null=False)
    last_check_at=models.DateTimeField(auto_now=timezone.now())
    
    def __str__(self):
        return self.site_name
    