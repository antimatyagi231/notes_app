# Generated by Django 3.2.7 on 2021-10-11 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
