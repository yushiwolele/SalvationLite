# Generated by Django 3.2.16 on 2023-09-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0006_alter_testcaseconfigmodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcaseconfigmodel',
            name='data_uuid',
            field=models.CharField(max_length=64, null=True, verbose_name='文件uuid'),
        ),
    ]