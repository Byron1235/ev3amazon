# Generated by Django 4.1.1 on 2022-12-05 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appLibros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='apellidoAutor',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='nombreAutor',
            new_name='nombre',
        ),
    ]