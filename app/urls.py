from django.urls import path
from .views import RoomList, BookingList,home, BookingView

app_name = 'app'

urlpatterns = [
    path('', home, name = 'home'),

    path('roomlist/', RoomList.as_view(), name = 'roomlist'),
    path('bookinglist/', BookingList.as_view(), name = 'bookinglist'),
    path('book/', BookingView.as_view(), name = 'bookingview'),

]