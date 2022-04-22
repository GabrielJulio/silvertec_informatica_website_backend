from django.db import models
from django.utils.translation import gettext_lazy as _


class Processor(models.Model):
    class Meta:
        verbose_name = _('processor')
        verbose_name_plural = _('processors')

    class BrandChoices(models.TextChoices):
        INTEL = 'INT', 'INTEL'
        AMD = 'AMD', 'AMD'

    name = models.CharField(_('name'), max_length=50)
    brand = models.CharField(
        _('brand'),
        max_length=3,
        blank=False,
        choices=BrandChoices.choices,
        default=BrandChoices.INTEL
    )

    def __str__(self) -> str:
        return self.name
