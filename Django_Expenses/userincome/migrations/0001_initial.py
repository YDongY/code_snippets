# Generated by Django 3.1.2 on 2020-10-06 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '收入来源',
                'verbose_name_plural': '收入来源',
            },
        ),
        migrations.CreateModel(
            name='UserIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='总收入')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('description', models.TextField(verbose_name='描述')),
                ('source', models.CharField(max_length=256, verbose_name='来源')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '收入记录',
                'verbose_name_plural': '收入记录',
                'ordering': ['-date'],
            },
        ),
    ]
