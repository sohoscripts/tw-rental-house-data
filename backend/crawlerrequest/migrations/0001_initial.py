# Generated by Django 2.0.7 on 2018-07-19 08:06

import crawlerrequest.enums
from django.db import migrations, models
import django.db.models.deletion
import rental.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField(default=rental.models.current_year)),
                ('month', models.IntegerField(default=rental.models.current_month)),
                ('day', models.IntegerField(default=rental.models.current_day)),
                ('hour', models.IntegerField(default=rental.models.current_stepped_hour)),
                ('request_type', models.IntegerField(choices=[(crawlerrequest.enums.RequestType(0), 0), (crawlerrequest.enums.RequestType(1), 1)])),
                ('seed', rental.models.JSONField()),
                ('is_pending', models.BooleanField(default=False)),
                ('last_status', models.IntegerField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rental.Vendor')),
            ],
            options={
                'db_table': 'request_ts',
            },
        ),
        migrations.AddIndex(
            model_name='requestts',
            index=models.Index(fields=['year', 'month', 'day', 'hour'], name='request_ts_year_d996ac_idx'),
        ),
    ]
