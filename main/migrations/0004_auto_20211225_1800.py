# Generated by Django 3.2.8 on 2021-12-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211225_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='postuser',
            name='fname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='postuser',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='postuser',
            name='surname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
