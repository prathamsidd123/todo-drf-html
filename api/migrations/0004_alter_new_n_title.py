# Generated by Django 5.2.1 on 2025-05-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_new_remove_task_ncompleted_remove_task_ntitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='n_title',
            field=models.CharField(max_length=200),
        ),
    ]
