from django.db import models

class Task(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone_num = models.CharField('Номер телефона', max_length=100)
    mail = models.CharField('почта', max_length=100)
    name_car = models.CharField('Название машины', max_length=100)
    task = models.TextField('Комментарий')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Арендовал'
        verbose_name_plural = 'Арендовали'