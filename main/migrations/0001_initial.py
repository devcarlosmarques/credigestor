# Generated by Django 4.2.7 on 2023-12-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.IntegerField()),
                ('proposta', models.CharField(max_length=255)),
                ('banco', models.CharField(max_length=255)),
                ('prazo', models.IntegerField()),
                ('valor', models.FloatField()),
                ('parcela', models.FloatField()),
            ],
        ),
    ]
