from django.test import SimpleTestCase
from core.forms import TicketForm

class TestForms(SimpleTestCase):
    
    def test_form_ticket_form_incorrect(self):
        form = TicketForm(data={
            'name': '',
            'cpf': 'asdasdasdads',
            'age': 0,
            'cont_numbers': 0
        })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_form_ticket_form_correct(self):
        form = TicketForm(data={
            'name': 'Fulano',
            'cpf': '616.064.683-40',
            'age': 18,
            'cont_numbers': 5
        })
        print(form.errors)        
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)