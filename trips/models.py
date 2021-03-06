from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.utils import TaxiAPI


class TripStatus:
    """ Утилитный клас, содержащий в себе статусы поездки """

    CREATED = 'CR'
    APPROVAL = 'AP'
    ACCEPTED = 'AC'
    DENIED = 'DE'
    COMPLETED = 'CO'
    
    CHOICES = (
        (CREATED, 'Создана'),
        (APPROVAL, 'На модерации'),
        (ACCEPTED, 'Принята'),
        (DENIED, 'Отклонена'),
        (COMPLETED, 'Завершена'),
    )


class Trip(models.Model):
    """ Модель поездки """

    class Meta:
        ordering = ['-created']

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trips')

    departure = models.CharField(verbose_name='Пункт отправления', max_length=140)
    arrival = models.CharField(verbose_name='Пункт назначения', max_length=140)
    purpose = models.CharField(verbose_name='Цель поездки', max_length=420)

    date = models.DateField(verbose_name='Дата поездки')
    departure_time = models.TimeField(verbose_name='Время отправления')
    arrival_time = models.TimeField(verbose_name='Время возврата', blank=True, null=True)

    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)
    status = models.CharField(verbose_name='Статус', max_length=2,
                              choices=TripStatus.CHOICES, default=TripStatus.CREATED)
    length = models.FloatField(verbose_name='Длина пути', blank=True, null=True)


@receiver(post_save, sender=Trip)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.status == TripStatus.CREATED:
        instance.length = TaxiAPI.get_length()
        instance.status = TripStatus.APPROVAL
        instance.save()
