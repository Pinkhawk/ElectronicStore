# Generated by Django 3.2.7 on 2021-12-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='mysite/myapp1/static/myappp1/images/logo.jpg', max_length=500),
        ),
    ]
