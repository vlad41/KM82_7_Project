# Generated by Django 3.2.8 on 2021-12-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postuser',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]