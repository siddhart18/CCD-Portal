# Generated by Django 2.2.5 on 2020-02-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_selected_students_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selected_students',
            name='name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Students'),
        ),
    ]