# Generated by Django 2.1.1 on 2019-01-18 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0012_eventmaster_under_which_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='roleassignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
