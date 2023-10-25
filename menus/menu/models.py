from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(
        'Name',
        max_length=256,
        blank=False,
        null=False
    )
    long_name = models.CharField(
        'Verbose_name',
        max_length=256,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.long_name


class Menu(models.Model):
    name = models.CharField(
        'Name',
        max_length=256,
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Категория'
    )
    link = models.CharField(
        'Link',
        max_length=256,
        blank=False,
        null=False
    )
    parent_item = models.ForeignKey(
        'self',
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        default=0,
        verbose_name='Parent element'
    )

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.name
