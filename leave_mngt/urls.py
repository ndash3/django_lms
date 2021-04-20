from django.urls import path
from leave_mngt.views import home,shiftrota_view
from django.conf.urls import url

#
urlpatterns = [
     path('',home,name='home'),
     url('shift',shiftrota_view,name='shift'),
]