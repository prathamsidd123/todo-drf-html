# Generated by Django 5.2.1 on 2025-05-30 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_task_details_rename_completed_new_n_completed_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
