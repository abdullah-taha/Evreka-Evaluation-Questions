# Generated by Django 3.1.1 on 2020-09-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evreka', '0002_auto_20200916_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navigationrecord',
            old_name='datatime',
            new_name='datetime',
        ),
    ]
