# Generated by Django 3.0.3 on 2020-03-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0002_auto_20200306_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=564, null=True, verbose_name='Titulo')),
                ('url', models.CharField(blank=True, max_length=564, null=True, verbose_name='URL')),
            ],
        ),
    ]