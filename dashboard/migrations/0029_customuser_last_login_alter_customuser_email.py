# Generated by Django 5.0.1 on 2024-02-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_document_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(
                blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=57, unique=True),
        ),
    ]
