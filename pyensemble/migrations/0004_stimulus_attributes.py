# Generated by Django 2.2.7 on 2020-04-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyensemble', '0003_auto_20200413_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='stimulus',
            name='attributes',
            field=models.ManyToManyField(through='pyensemble.StimulusXAttribute', to='pyensemble.Attribute'),
        ),
    ]
