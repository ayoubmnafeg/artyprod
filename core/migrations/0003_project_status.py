# Generated by Django 4.2.1 on 2023-05-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_owner_project_responsibles_project_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('IR', 'In Review'), ('P', 'Pending'), ('C', 'Completed'), ('CL', 'Cancelled'), ('IP', 'In Progress')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
