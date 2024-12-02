from django.urls import path
from ride.views import *
app_name='nothing'

urlpatterns=[
    path('auto/',auto,name='auto'),
]