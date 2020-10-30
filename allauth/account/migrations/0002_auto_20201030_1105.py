# Generated by Django 3.0.4 on 2020-10-30 11:05

import allauth.account.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='email',
            field=allauth.account.fields.SearchFieldAllowIExact(blank=True, db_index=True, encrypted_field_name='_email', hash_key='659fc7d0793339b54c70a896aab89162d4d3b039a3e59bb2c79b65a2c3cb5ba8', max_length=66, null=True, verbose_name='e-mail address'),
        ),
    ]
