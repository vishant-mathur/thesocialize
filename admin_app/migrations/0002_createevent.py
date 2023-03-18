# Generated by Django 4.0.5 on 2023-03-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20)),
                ('event_address', models.CharField(max_length=200)),
                ('date_time', models.DateField()),
                ('event_dis', models.CharField(max_length=300)),
                ('event_type', models.CharField(choices=[('parties', 'PARTIES'), ('meetings', 'MEETINGS'), ('seminars', 'seminars')], max_length=50)),
            ],
        ),
    ]
