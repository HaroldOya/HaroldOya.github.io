# Generated by Django 2.2.16 on 2020-10-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Maipo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productor',
            old_name='telofono',
            new_name='telefono',
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('fechaPublicacion', models.DateTimeField()),
                ('dueñoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Maipo.Productor')),
            ],
        ),
    ]