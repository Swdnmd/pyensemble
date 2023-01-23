# Generated by Django 3.1.14 on 2023-01-23 22:29

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyensemble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='session_diagnostic_script',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='experimentxattribute',
            name='attribute_value_double',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experimentxattribute',
            name='attribute_value_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='session',
            name='diagnostics_data',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='session',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='StudyXExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_order', models.PositiveSmallIntegerField()),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyensemble.experiment')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyensemble.study')),
            ],
            options={
                'unique_together': {('study', 'experiment', 'experiment_order')},
            },
        ),
    ]
