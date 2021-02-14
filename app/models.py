from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy
import datetime
# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('suit','suit'),
        ('delux','delux'),
        ('normal','normal'),
    )
    room_mumber = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.room_mumber}, {self.category} room with {self.beds} beds for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

