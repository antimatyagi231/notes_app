# Generated by Django 3.2.7 on 2021-10-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_signupform_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.EmailField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
