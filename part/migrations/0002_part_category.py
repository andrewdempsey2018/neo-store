# Generated by Django 3.0.3 on 2020-02-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]
