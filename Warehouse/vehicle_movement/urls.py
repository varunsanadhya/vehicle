from django.conf.urls import url
from vehicle_movement import views

app_name = 'vehicle_movement'
urlpatterns = [
    url(r'^checkinview/',views.CheckinView, name = 'checkinview'),
    url(r'^listView/',views.listView, name = 'listView'),
]
