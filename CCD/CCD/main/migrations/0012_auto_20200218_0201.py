# Generated by Django 2.2.5 on 2020-02-17 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200218_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selected_students',
            name='name',
            field=models.OneToOneField(default='', max_length=40, on_delete=django.db.models.deletion.CASCADE, to='main.Students'),
        ),
    ]