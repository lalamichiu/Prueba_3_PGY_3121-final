# Generated by Django 3.2.6 on 2022-06-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_alter_producto_nuevo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='id_marca',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Marca'),
        ),
    ]
