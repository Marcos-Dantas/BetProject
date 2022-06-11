from django.shortcuts import render
from core.forms import TicketForm
from django.http import HttpResponse
from core.models import Ticket

from django_xhtml2pdf.utils import generate_pdf

def response_pdf(new_ticket):
    resp = HttpResponse(content_type='application/pdf')
    resp['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    resp = generate_pdf('ticket.html', file_object=resp, context={'new_ticket': new_ticket})

    return resp


def homepage_view(request):  
    return render(request, 'home.html', context={'form': TicketForm()})

def generate_ticket(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        numbers = Ticket.generate_numbers( int( request.POST.get('cont_numbers')))
        new_ticket = form.save(commit=False)
        new_ticket.list_numbers = {'numbers': numbers}
        new_ticket.save()

        return response_pdf(new_ticket)
    else:
        return render(request, 'home.html', context={'form': form})    