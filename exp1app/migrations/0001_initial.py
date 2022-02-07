# Generated by Django 3.2.12 on 2022-02-06 10:10

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
            name='SamplingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('animal', models.TextField(null=True)),
                ('purpose', models.TextField(null=True)),
                ('method', models.TextField(null=True)),
                ('control_number', models.TextField(null=True)),
                ('control_situation', models.TextField(null=True)),
                ('experiment_number', models.TextField(null=True)),
                ('experiment_situation', models.TextField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(null=True)),
                ('suggestion', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Animal', models.CharField(max_length=100, null=True)),
                ('purpose', models.TextField(null=True)),
                ('manager', models.TextField(null=True)),
                ('wash', models.TextField(null=True)),
                ('wash_frequency', models.TextField(null=True)),
                ('feed', models.TextField(null=True)),
                ('feed_frequency', models.TextField(null=True)),
                ('temprature', models.TextField(null=True)),
                ('location', models.TextField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
