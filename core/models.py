from django.db import models
import uuid
import random

class Ticket(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    age = models.IntegerField('Idade')
    cont_numbers = models.IntegerField('Quantidade de Numeros')
    list_numbers = models.JSONField()
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, default='page-slug')
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    
    def get_formated_numbers(self):
        """
            retorna o valor da lista de numeros gerados, como uma string
        """
        numbers = list( self.list_numbers.values())[0]
        string_ints = [str(num) for num in numbers]
        str_of_ints = ",".join(string_ints)
        
        return str_of_ints
    
    def generate_numbers(cont_numbers):
        """
            gerar numeros randomicos e retorna uma lista
        """
        numbers = random.sample(range(1,80), cont_numbers)      
        return numbers

    def get_formated_date(self):
        """
            pegar valor da data no formato correto
        """
        return self.create_date.strftime('%d/%m/%Y %H:%M:%S')
 
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(*args, **kwargs)