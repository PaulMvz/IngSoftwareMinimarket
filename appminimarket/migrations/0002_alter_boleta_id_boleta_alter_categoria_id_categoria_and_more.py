# Generated by Django 4.1.7 on 2023-02-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appminimarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='id_boleta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id_categoria',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detalleboleta',
            name='id_detalleboleta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
