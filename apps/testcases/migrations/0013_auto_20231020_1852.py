# Generated by Django 3.2.16 on 2023-10-20 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0012_scriptconfig_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestCaseConfigTemplateFormat',
        ),
        migrations.DeleteModel(
            name='TestCaseConfigTemplateWidget',
        ),
    ]