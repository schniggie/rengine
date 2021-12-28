# Generated by Django 3.2.4 on 2021-12-27 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubScan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_scan_date', models.DateTimeField()),
                ('scan_status', models.IntegerField()),
                ('celery_id', models.CharField(blank=True, max_length=100)),
                ('dir_file_search', models.BooleanField(default=False, null=True)),
                ('port_scan', models.BooleanField(default=False, null=True)),
                ('fetch_url', models.BooleanField(default=False, null=True)),
                ('vulnerability_scan', models.BooleanField(default=False, null=True)),
                ('osint', models.BooleanField(default=False, null=True)),
                ('stop_scan_date', models.DateTimeField(blank=True, null=True)),
                ('scan_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startScan.scanhistory')),
                ('subdomain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startScan.subdomain')),
            ],
        ),
    ]