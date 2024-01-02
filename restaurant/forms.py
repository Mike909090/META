from django import forms    
from .models import Bookings
from django.forms import ModelForm
from .models import MenuItem

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = "__all__"

class MenuForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['item_name', 'category', 'description']