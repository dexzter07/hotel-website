from django.urls import path
from .views import RoomList, BookingList

app_name = 'app'

urlpatterns = [
    path('roomlist/', RoomList.as_view(), name = 'roomlist'),
    path('bookinglist/', BookingList.as_view(), name = 'bookinglist'),
]