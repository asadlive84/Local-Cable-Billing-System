# Generated by Django 3.0.1 on 2019-12-22 20:27

import clients.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union_name', models.CharField(max_length=100)),
                ('union_number', models.IntegerField()),
                ('help_info', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=100)),
                ('word_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('union', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.Union')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, default=clients.models.create_client_id, max_length=10, unique=True, verbose_name='Client ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('mobile_number', models.PositiveIntegerField(unique=True, verbose_name='Mobile Number')),
                ('others_number', models.PositiveIntegerField(verbose_name="Other's Number")),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10, verbose_name='Gender')),
                ('address', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word_union', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Word')),
            ],
        ),
    ]
