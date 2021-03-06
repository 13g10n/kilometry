# Generated by Django 2.0 on 2017-12-03 18:09

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
            name='FamilyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trips_per_month', models.PositiveIntegerField(verbose_name='Необходимое количество поездок в месяц')),
                ('car_requirements', models.TextField(verbose_name='Требования к машине')),
                ('info', models.TextField(blank=True, max_length=500, verbose_name='Дополнительно')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
