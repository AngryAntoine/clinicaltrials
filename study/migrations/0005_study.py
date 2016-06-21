# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-08 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20160601_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinical_study_sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.ClinicalStudySite')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Contacts')),
                ('eligibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Eligibility')),
                ('general_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.GeneralInformation')),
                ('study_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.StudyIdentifiers')),
            ],
            options={
                'verbose_name': 'study',
                'verbose_name_plural': 'studies',
            },
        ),
    ]
