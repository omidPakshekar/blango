# Generated by Django 3.2.14 on 2022-07-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0002_auto_20220704_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
