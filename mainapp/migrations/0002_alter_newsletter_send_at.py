# Generated by Django 5.1.7 on 2025-03-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='send_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
