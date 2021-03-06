# Generated by Django 2.1.5 on 2019-05-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20190505_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstudyrating',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userstudyrating',
            name='musical_culture',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userstudyrating',
            name='serial_no',
            field=models.IntegerField(default=77552330, primary_key=True, serialize=False),
        ),
    ]
