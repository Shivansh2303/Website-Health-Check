from django.contrib import admin
from django.urls import path,include
from django_serverless_cron import urls as django_serverless_cron_urls


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from dashboard import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cron/', include(django_serverless_cron_urls)),
    path("dashboard/",views.SiteCreateAPIView().as_view(),name='home'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    
]
