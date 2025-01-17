# Generated by Django 2.2.24 on 2023-12-19 10:57

from django.db import migrations


def get_apartments(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        flat = Flat.objects.filter(owner=owner.name, owners_phonenumber=owner.phonenumber)
        owner.flats.set(flat)



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20231219_1853'),
    ]

    operations = [
        migrations.RunPython(get_apartments)
    ]
