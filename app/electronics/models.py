from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, editable=False, **NULLABLE,
                             verbose_name='Сотрудник')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=50, **NULLABLE, verbose_name='Улица')
    house_number = models.PositiveIntegerField(**NULLABLE, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, editable=False, **NULLABLE,
                            verbose_name='Сотрудник')
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=100, **NULLABLE, verbose_name='Модель')
    date = models.DateTimeField(verbose_name='Дата выхода')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Supplier(models.Model):
        FACTORY = 'FACTORY'
        RETAIL = 'RETAIL'
        ENTREPRENEUR = 'ENTREPRENEUR'

        SUPPLY_CHAIN = (
            (FACTORY, 'Завод'),
            (RETAIL, 'Розничная сеть'),
            (ENTREPRENEUR, 'Индивидуальный предприниматель')
        )

        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, editable=False, **NULLABLE,
                            verbose_name='Сотрудник')
        level = models.CharField(max_length=50, choices=SUPPLY_CHAIN)
        title = models.CharField(max_length=150, verbose_name='Название')
        contact = models.ForeignKey('electronics.Contact', on_delete=models.SET_NULL, **NULLABLE,
                                    verbose_name='Контакты')
        product = models.ForeignKey('electronics.Product', on_delete=models.SET_NULL, **NULLABLE,
                                        verbose_name='Продукты')
        chain = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
        debt = models.FloatField(**NULLABLE, verbose_name='Задолженность')
        creat_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

        class Meta:
            verbose_name = 'Поставщик'
            verbose_name_plural = 'Поставщики'

        def __str__(self):
            return self.title
