from django.db import models


class Resume(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    number = models.BigIntegerField(verbose_name='Номер телефона')
    email = models.EmailField()
    department = models.CharField(max_length=50, verbose_name='Направление')
    description = models.TextField(verbose_name='Описание')
    experience = models.TextField(verbose_name='Опыт')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
