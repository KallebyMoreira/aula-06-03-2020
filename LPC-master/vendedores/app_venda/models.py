from django.db import models

    

class Vendedor(models.Model):
    class Meta:
        
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
    cpf = models.CharField('Cpf',max_length = 11,blank=True, null=True)
    nome =models.CharField('Nome',max_length = 150,blank=True, null=True)
    valor_venda = models.FloatField('Valor das vendas',max_length = 150,blank=True, null=True)
    qt_hr_trabalhadas = models.IntegerField('Quantidade de horas trabalhada',max_length = 150,blank=True, null=True)
    
    
    

    def Calculo(self,valor_venda,qt_hr_trabalhadas):
        self.calc_t = qt_hr_trabalhadas * 50
        self.calc_v = valor_venda * 0.05
        self.total = self.calc_t + self.calc_v
        return self.total
        
   
    
    
    def __str__(self):
            return self.nome

    