from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Project(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200,
                               verbose_name=_("Título")),
        description=models.TextField(
            verbose_name=_("Descripción")),
    )
    image = models.ImageField(verbose_name=_("Imagen"), upload_to="projects")
    link = models.URLField(null=True, blank=True,
                           verbose_name=_("Dirección Web"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Fecha de creación"))
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name=_("Fecha de edición"))

    class Meta:
        verbose_name = _("proyecto")
        verbose_name_plural = _("proyectos")
        ordering = ["-created"]

    def __str__(self):
        return self.title
