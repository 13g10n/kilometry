# Generated by Django 2.0 on 2017-12-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='car_requirements',
            field=models.TextField(blank=True, verbose_name='Требования к машине'),
        ),
        migrations.AlterField(
            model_name='familyprofile',
            name='trips_per_month',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Необходимое количество поездок в месяц'),
        ),
    ]