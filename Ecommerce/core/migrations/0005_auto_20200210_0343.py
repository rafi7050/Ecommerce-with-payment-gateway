# Generated by Django 2.2.4 on 2020-02-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200210_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='YI',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Yearly Income'),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='age',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Age'),
        ),
    ]