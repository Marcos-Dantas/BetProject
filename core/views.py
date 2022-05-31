from django.shortcuts import render
from core.forms import TicketForm
import random
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def response_pdf(new_ticket):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    
    p = canvas.Canvas(response)
    
    p.drawString(200, 500, "Ticket Loteria Brazil ") 
    p.drawString(200, 485, "Nome: " + new_ticket.name) 
    p.drawString(200, 470, "CPF: " + new_ticket.cpf) 
    p.drawString(200, 455, "Idade: " + str(new_ticket.age)) 
    p.drawString(200, 440, "Quantidade de Numeros: " + str(new_ticket.cont_numbers)) 
    p.drawString(200, 425, "Numeros: " + new_ticket.get_formated_numbers()) 
    p.drawString(200, 410, "Data de Criação: " + new_ticket.get_formated_date() ) 
    

    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    return response

def homepage_view(request):  
    return render(request, 'base.html', context={'form': TicketForm()})

def generate_numbers(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        cont_numbers = int(request.POST.get('cont_numbers'))
        numbers = random.sample(range(100), cont_numbers)
        new_ticket = form.save(commit=False)
        new_ticket.list_numbers = {'numbers': numbers}
        new_ticket.save()

        return response_pdf(new_ticket)

    return render(request, 'result.html', context={'ticket': False})

    