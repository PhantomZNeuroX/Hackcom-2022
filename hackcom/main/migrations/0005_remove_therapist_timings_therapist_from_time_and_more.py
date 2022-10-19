# Generated by Django 4.1.2 on 2022-10-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_therapist_timings_alter_therapist_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapist',
            name='timings',
        ),
        migrations.AddField(
            model_name='therapist',
            name='from_time',
            field=models.CharField(default='24x7', max_length=50),
        ),
        migrations.AddField(
            model_name='therapist',
            name='to_time',
            field=models.CharField(default='24x7', max_length=50),
        ),
    ]