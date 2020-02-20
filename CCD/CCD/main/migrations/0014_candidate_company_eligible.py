# Generated by Django 2.2.5 on 2020-02-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200218_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(blank=True, max_length=200)),
                ('expected_time', models.CharField(blank=True, max_length=200)),
                ('candidate_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('roll_number', models.CharField(max_length=50)),
                ('is_selected', models.BooleanField(default=False)),
                ('is_interview', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='eligible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpi', models.CharField(blank=True, max_length=100)),
                ('major', models.CharField(blank=True, max_length=100)),
                ('minor', models.BooleanField(blank=True, default=False)),
                ('programme', models.CharField(choices=[('btech', 'btech'), ('mtech', 'mtech'), ('msc', 'msc'), ('mdes', 'mdes'), ('bdes', 'bdes'), ('phd', 'phd'), ('msr', 'msr'), ('ma', 'ma')], max_length=100)),
                ('specialization', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('cpoc', models.CharField(max_length=200)),
                ('cpoc_contact', models.CharField(max_length=200)),
                ('all_candidate', models.ManyToManyField(blank=True, related_name='all_person', to='main.candidate')),
                ('eligibility_criteria', models.ManyToManyField(related_name='eligible_companies', to='main.eligible')),
                ('shortlist_candidate', models.ManyToManyField(blank=True, related_name='shortlist_person', to='main.candidate')),
                ('waiting_candidate', models.ManyToManyField(blank=True, related_name='waiting_person', to='main.candidate')),
            ],
        ),
    ]
