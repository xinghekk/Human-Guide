# Generated by Django 2.1.4 on 2020-10-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0005_truth_label'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='truth',
            options={'ordering': ('-label',)},
        ),
        migrations.AlterField(
            model_name='truth',
            name='Truth',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='truth',
            name='reason',
            field=models.TextField(),
        ),
    ]
