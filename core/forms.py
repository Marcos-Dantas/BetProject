from django import forms 
from core.models import Ticket
import re

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['slug', 'create_date', 'list_numbers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['cpf'].required = False
        self.fields['age'].required = False
        self.fields['cont_numbers'].required = False
    
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) == 0 or name == None:
            self._errors['name'] = self.error_class([
                'Informe um nome válido.'
            ])
        
        return self.cleaned_data

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')      

        # verificar se o cpf esta no padrão correto NNN.NNN.NNN-NN 
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            self._errors['cpf'] = self.error_class([
                'Informe um cpf válido.'
            ])

            return self.cleaned_data

        
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        
        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            self._errors['cpf'] = self.error_class([
                'Informe um cpf válido.'
            ])
        
        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            self._errors['cpf'] = self.error_class([
                'Informe um cpf válido.'
            ])
        
        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            self._errors['cpf'] = self.error_class([
                'Informe um cpf válido.'
            ])  
    
        return self.cleaned_data

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age == None or age <= 0:
            self._errors['age'] = self.error_class([
                'Informe uma idade válida.'
            ])

        return self.cleaned_data

    def clean_cont_numbers(self):
        cont_numbers = self.cleaned_data.get('cont_numbers')

        if cont_numbers == None or cont_numbers <= 0:
            self._errors['cont_numbers'] = self.error_class([
                'Informe um valor válido.'
            ])

        return self.cleaned_data