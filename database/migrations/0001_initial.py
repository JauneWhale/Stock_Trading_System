# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 22:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountID', models.CharField(max_length=20)),
                ('Password', models.CharField(default='0', max_length=20)),
                ('Isfirst', models.BooleanField(default=1)),
                ('BuyPassword', models.CharField(default='0', max_length=20)),
                ('loginPwdWrongNum', models.IntegerField(default=0)),
                ('transPwdWrongNum', models.IntegerField(default=0)),
                ('lastTimeTrans', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 313421, tzinfo=utc))),
                ('lastTimeLogin', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 313457, tzinfo=utc))),
                ('IsTransFreeze', models.BooleanField(default=0)),
                ('IsLoginFreeze', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CapitalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountID', models.CharField(max_length=20)),
                ('ActiveMoney', models.FloatField(default=0)),
                ('FrozenMoney', models.FloatField(default=0)),
                ('BankCard', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InstDealed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstID', models.CharField(max_length=20)),
                ('TimeSubmit', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 314209, tzinfo=utc))),
                ('TimeDealed', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 314242, tzinfo=utc))),
                ('InstType', models.IntegerField(default=0)),
                ('StockID', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField(default=1)),
                ('PriceSubmit', models.FloatField(default=0)),
                ('PriceDealed', models.FloatField(default=0)),
                ('AccountID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CapitalAccountInfo')),
            ],
        ),
        migrations.CreateModel(
            name='InstNotDealed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstID', models.CharField(max_length=20)),
                ('TimeSubmit', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 315245, tzinfo=utc))),
                ('TimeOutOfDate', models.DateTimeField(default=datetime.datetime(2016, 6, 28, 22, 44, 53, 315278, tzinfo=utc))),
                ('InstType', models.IntegerField(default=0)),
                ('InstState', models.IntegerField(default=0)),
                ('StockID', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField(default=1)),
                ('PriceSubmit', models.FloatField(default=0)),
                ('AccountID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.CapitalAccountInfo')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SecurityID', models.CharField(max_length=20)),
                ('IsFreeze', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityStockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SecurityID', models.CharField(max_length=20)),
                ('StockID', models.CharField(max_length=20)),
                ('ShareHolding', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('BuyPrice', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StaffTable',
            fields=[
                ('StuffID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('StuddName', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StockName', models.TextField()),
                ('StockID', models.CharField(max_length=20)),
                ('CurrentPrice', models.FloatField(default=0)),
                ('MaxPrice', models.FloatField(default=0)),
                ('MinPrice', models.FloatField(default=0)),
                ('TodayOpeningPrice', models.FloatField(default=0)),
                ('YesterdayClosingPrice', models.FloatField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('UpLimit', models.FloatField(default=0)),
                ('BottomLimit', models.FloatField(default=0)),
                ('State', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StockManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('IDcard', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Gender', models.IntegerField(default=0)),
                ('Occupation', models.CharField(default='0', max_length=20)),
                ('EduInfo', models.CharField(default='0', max_length=20)),
                ('HomeAddr', models.TextField(default='0')),
                ('Department', models.TextField(default='0')),
                ('Tel', models.CharField(default='0', max_length=20)),
                ('MailAddr', models.CharField(default='0', max_length=30)),
                ('Age', models.IntegerField(default='0')),
            ],
        ),
        migrations.AddField(
            model_name='stockmanage',
            name='AdminID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='database.UserTable'),
        ),
        migrations.AddField(
            model_name='stockmanage',
            name='StockID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='database.StockInfo'),
        ),
        migrations.AddField(
            model_name='securityaccountinfo',
            name='IDcard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.UserTable'),
        ),
        migrations.AddField(
            model_name='instnotdealed',
            name='SecurityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.SecurityAccountInfo'),
        ),
        migrations.AddField(
            model_name='instdealed',
            name='SecurityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.SecurityAccountInfo'),
        ),
        migrations.AddField(
            model_name='capitalaccountinfo',
            name='SecurityAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.SecurityAccountInfo'),
        ),
        migrations.AddField(
            model_name='capitalaccountinfo',
            name='UserTable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.UserTable'),
        ),
    ]
