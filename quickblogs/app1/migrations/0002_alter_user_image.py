# Generated by Django 5.1.1 on 2024-10-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, default='dp.png', null=True, upload_to=''),
        ),
    ]
