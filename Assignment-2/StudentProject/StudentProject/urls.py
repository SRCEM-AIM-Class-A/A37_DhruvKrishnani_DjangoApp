from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),  # Homepage from app1
    path('app2/', include('app2.urls')),
]
