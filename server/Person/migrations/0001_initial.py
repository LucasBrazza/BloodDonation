# Generated by Django 4.2.10 on 2024-02-12 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BloodType', '0001_initial'),
        ('City', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=12, unique=True)),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=4)),
                ('complement', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('bloodTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BloodType.bloodtype')),
                ('cityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='City.city')),
            ],
        ),
    ]
