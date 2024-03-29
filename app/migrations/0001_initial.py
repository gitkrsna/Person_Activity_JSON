# Generated by Django 3.1.1 on 2020-09-26 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('real_name', models.CharField(blank=True, max_length=20)),
                ('tz', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_activity', to='app.user')),
            ],
        ),
    ]
