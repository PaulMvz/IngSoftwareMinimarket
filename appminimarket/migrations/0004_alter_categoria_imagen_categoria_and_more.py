# Generated by Django 4.1.7 on 2023-02-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appminimarket', '0003_rename_direccion_boleta_boleta_nombrecliente_boleta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen_categoria',
            field=models.ImageField(blank=True, null=True, upload_to='Categorias'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='Productos'),
        ),
    ]
