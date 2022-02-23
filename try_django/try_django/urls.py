
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('easy_votings.urls')),
    path('easy_votings/', include('easy_votings.urls')),
]