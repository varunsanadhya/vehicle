from django import forms
from django.forms import ModelForm
from vehicle_movement.models import Checkin

class CheckinForm(forms.ModelForm):
    class Meta():
        model = Checkin
        fields = ('vehicle_num','Driver_name','BusinessUnit','Type')
