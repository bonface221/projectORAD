# Generated by Django 5.0.1 on 2024-01-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
