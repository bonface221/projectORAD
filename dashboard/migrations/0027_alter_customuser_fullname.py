# Generated by Django 5.0.1 on 2024-02-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_alter_customuser_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]