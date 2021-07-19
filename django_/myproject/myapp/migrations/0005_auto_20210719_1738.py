# Generated by Django 3.2.3 on 2021-07-19 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_community_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='body',
            field=models.TextField(default='', verbose_name='CONTENT'),
        ),
        migrations.AlterField(
            model_name='community',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='PUBLISH DATE'),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=300, verbose_name='TITlE'),
        ),
    ]