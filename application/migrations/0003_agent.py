# Generated by Django 4.1.3 on 2022-11-29 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0002_delete_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('branch', models.CharField(max_length=256)),
                ('is_student', models.BooleanField(default=True)),
                ('user_id', models.IntegerField()),
                ('lab_code', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
