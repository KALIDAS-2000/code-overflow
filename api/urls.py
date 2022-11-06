from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import *


router=DefaultRouter()



urlpatterns=[

]+router.urls