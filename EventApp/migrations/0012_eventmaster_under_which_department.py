# Generated by Django 2.1.5 on 2019-01-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0011_auto_20190116_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmaster',
            name='under_which_department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EventApp.Department'),
            preserve_default=False,
        ),
    ]
