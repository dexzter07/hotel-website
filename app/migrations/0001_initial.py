# Generated by Django 3.0.7 on 2021-02-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_mumber', models.IntegerField()),
                ('category', models.CharField(choices=[('suit', 'suit'), ('delux', 'delux'), ('normal', 'normal')], max_length=10)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
