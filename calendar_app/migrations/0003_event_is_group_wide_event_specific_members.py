# Generated by Django 5.1.6 on 2025-03-15 18:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0002_calendargroup_event_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_group_wide',
            field=models.BooleanField(default=True, help_text='If checked, event is for all group members'),
        ),
        migrations.AddField(
            model_name='event',
            name='specific_members',
            field=models.ManyToManyField(blank=True, related_name='assigned_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
