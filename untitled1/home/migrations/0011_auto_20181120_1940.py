# Generated by Django 2.1.3 on 2018-11-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181120_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='facid',
            field=models.CharField(default='NULL', max_length=10, primary_key=True, serialize=False),
        ),
    ]