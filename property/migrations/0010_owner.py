# Generated by Django 2.2.24 on 2023-12-12 19:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20231211_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца:')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца:')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности:')),
            ],
        ),
    ]
