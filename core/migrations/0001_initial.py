# Generated by Django 4.0 on 2021-12-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('views', models.IntegerField(blank=True)),
                ('clicks', models.IntegerField(blank=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
            ],
        ),
    ]
