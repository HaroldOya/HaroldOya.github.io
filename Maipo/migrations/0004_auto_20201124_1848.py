# Generated by Django 3.1.2 on 2020-11-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maipo', '0003_auto_20201124_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(upload_to='\\static\\img\\products'),
        ),
    ]
