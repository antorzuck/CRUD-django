from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update')
]
