# Generated by Django 3.1.2 on 2020-11-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maipo', '0002_auto_20201123_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(upload_to='../static/img/products/'),
        ),
    ]
