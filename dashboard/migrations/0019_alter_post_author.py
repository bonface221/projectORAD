# Generated by Django 5.0.1 on 2024-02-01 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_post_document_remove_post_profile_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.customuser'),
        ),
    ]
