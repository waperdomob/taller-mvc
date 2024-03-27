# Generated by Django 5.0.3 on 2024-03-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('id_number', models.BigIntegerField(default=0, verbose_name='Número de documento')),
                ('email', models.CharField(max_length=100)),
                ('birthdate', models.DateField(null=True, verbose_name='Fecha de nacimiento')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='fecha de registro')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]