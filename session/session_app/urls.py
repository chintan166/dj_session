from django.urls import path
from .views import set_session,del_session

urlpatterns = [
    path('setsession/', set_session, name='set_session'),
    path('delsession/', del_session, name='del_session'),
]