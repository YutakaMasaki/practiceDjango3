# Generated by Django 3.2.8 on 2021-10-31 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default=django.utils.timezone.now, max_length=140, verbose_name='本文'),
            preserve_default=False,
        ),
    ]