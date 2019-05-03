# Generated by Django 2.1.5 on 2019-05-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190503_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstudyrating',
            old_name='rating_1',
            new_name='rating1_1',
        ),
        migrations.RenameField(
            model_name='userstudyrating',
            old_name='rating_2',
            new_name='rating1_2',
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='musical_culture',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating2_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating2_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating3_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating3_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating4_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating4_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating5_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='rating5_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstudyrating',
            name='years_musical_training',
            field=models.IntegerField(default=0),
        ),
    ]
