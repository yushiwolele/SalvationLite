# Generated by Django 3.2.16 on 2023-09-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0008_scriptconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptconfig',
            name='level',
            field=models.IntegerField(default=0, null=True, verbose_name='文件级别'),
        ),
        migrations.AlterField(
            model_name='scriptconfig',
            name='path',
            field=models.CharField(max_length=1024, null=True, verbose_name='文件路径'),
        ),
    ]
