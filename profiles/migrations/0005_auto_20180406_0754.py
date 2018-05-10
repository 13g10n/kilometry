# Generated by Django 2.0 on 2018-04-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20171213_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=30, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='trips_per_month',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='Необходимое количество поездок в месяц'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('STAFF', 'Сотрудник'), ('BENEFACTOR', 'Благотворитель'), ('FAMILY', 'Семья')], default='BENEFACTOR', max_length=15),
        ),
    ]
