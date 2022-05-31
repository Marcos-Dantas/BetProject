from django import forms 
from core.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['slug', 'create_date', 'list_numbers']

