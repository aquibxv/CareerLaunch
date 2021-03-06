# Generated by Django 2.2 on 2020-01-30 14:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('salary', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=225)),
                ('upload_date', models.DateField(default=datetime.datetime.now)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
