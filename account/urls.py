from django.urls import path
from account.views import signup_view,login_view,signout_view
from django.conf.urls import url
#
urlpatterns = [
    url('signup', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    url('logout', signout_view, name='logout'),
 ]