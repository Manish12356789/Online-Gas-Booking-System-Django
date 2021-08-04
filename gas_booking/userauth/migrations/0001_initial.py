# Generated by Django 3.2.4 on 2021-07-27 06:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_name', models.CharField(help_text='Your store name.', max_length=1024, null=True)),
                ('mobile_phone', models.CharField(help_text='Enter Your mobile number without country code.', max_length=10)),
                ('address', models.CharField(help_text='Your street name and house number.', max_length=1024, null=True)),
                ('zip_code', models.CharField(max_length=12, null=True)),
                ('city', models.CharField(max_length=1024, null=True)),
                ('state', models.CharField(max_length=1024, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, help_text='Your stores website url if you have.', null=True, verbose_name='Website')),
                ('proof_pic', models.ImageField(blank=True, help_text='Your Id proof must have pan card.', null=True, upload_to='', verbose_name='Pan Card ')),
                ('additional_information', models.CharField(max_length=4096, null=True, verbose_name='Additional information')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='distributor', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', models.CharField(help_text='Enter Your mobile number without country code.', max_length=10, null=True, unique=True)),
                ('address', models.CharField(help_text='Your street name and house number.', max_length=1024, null=True)),
                ('zip_code', models.CharField(max_length=12, null=True)),
                ('city', models.CharField(max_length=1024, null=True)),
                ('state', models.CharField(max_length=1024, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('additional_information', models.CharField(max_length=4096, null=True, verbose_name='Additional information')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
