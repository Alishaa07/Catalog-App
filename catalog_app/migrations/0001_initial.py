# Generated by Django 4.2.3 on 2023-07-29 10:33

import catalog_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('colour', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=catalog_app.models.upload_to)),
            ],
        ),
    ]
