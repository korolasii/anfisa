# Generated by Django 2.2.19 on 2023-06-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('name',), 'verbose_name': 'мороженое', 'verbose_name_plural': 'мороженое'},
        ),
    ]
