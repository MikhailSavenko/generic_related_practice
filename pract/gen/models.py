from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Изнбранные"
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "content_type", "object_id"],
                name="unique_user_content_type_object_id"
            )
        ]


class Company(models.Model):
    name = models.CharField(max_length=100)
    favorites = GenericRelation(Favorite)


class Application(models.Model):
    name = models.CharField(max_length=100)
    favorites = GenericRelation(Favorite)
