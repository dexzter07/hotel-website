from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('suit','suit'),
        ('delux','delux'),
        ('normal','normal'),
    )
    room_category = forms.ChoiceField(choices = ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])

