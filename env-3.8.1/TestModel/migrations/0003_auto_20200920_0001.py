# Generated by Django 2.2.11 on 2020-09-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20200919_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Truth', models.CharField(max_length=120)),
                ('reason', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Truth1',
        ),
    ]
