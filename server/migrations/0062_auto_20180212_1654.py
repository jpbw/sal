# Generated by Django 1.10 on 2018-02-12 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0061_auto_20180210_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinedetailplugin',
            name='type',
            field=models.CharField(choices=[(b'machine_detail', b'Machine Detail')], default=b'machine_detail', max_length=255),
        ),
    ]
