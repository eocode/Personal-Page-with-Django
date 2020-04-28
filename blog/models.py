from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100,
                              verbose_name=_("Nombre"))
    )
    image = models.ImageField(upload_to="blog", null=True, blank=True,
                              verbose_name=_("Imagen"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Fecha de creación"))
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name=_("Fecha de edición"))

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200,
                               verbose_name=_("Título")),
        content=models.TextField(
            verbose_name=_("Contenido"))
    )
    published = models.DateTimeField(default=now,
                                     verbose_name=_("Fecha de publicación"))
    image = models.ImageField(upload_to="blog", null=True, blank=True,
                              verbose_name=_("Imagen"))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name=_("Autor"))
    categories = models.ManyToManyField(Category,
                                        verbose_name=_("Categorías"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Fecha de creación"))
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name=_("Fecha de edición"))

    class Meta:
        verbose_name = _("entrada")
        verbose_name_plural = _("entradas")
        ordering = ['-created']

    def __str__(self):
        return self.title
