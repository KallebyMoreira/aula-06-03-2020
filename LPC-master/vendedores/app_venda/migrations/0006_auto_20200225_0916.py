# Generated by Django 3.0.3 on 2020-02-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_venda', '0005_auto_20200225_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='qt_hr_trabalhadas',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Quantidade de horas trabalhada'),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='valor_venda',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Valor das vendas'),
        ),
    ]
