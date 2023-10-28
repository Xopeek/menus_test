from django.db import models


class TreeMenuCategory(models.Model):
    name = models.CharField(
        "Name",
        max_length=255,
        blank=False,
        null=False
    )
    verbose_name = models.CharField(
        "Verbose name",
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = "Menu category"
        verbose_name_plural = "Menu categories"

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):
    name = models.CharField(
        "Name",
        max_length=255,
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        TreeMenuCategory,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Category"
    )
    path = models.CharField(
        "Link",
        max_length=1000,
        blank=False,
        null=False
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0,
        verbose_name="Parent element"
    )

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def __str__(self):
        return self.name
