# Generated by Django 5.1.7 on 2025-03-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('path', models.ImageField(upload_to='productos/')),
            ],
        ),
    ]
