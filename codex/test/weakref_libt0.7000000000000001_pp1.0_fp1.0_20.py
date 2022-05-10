import weakref
from operator import attrgetter

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    ManyToManyField,
    ForeignKey,
    OneToOneField,
    CASCADE,
    SET_NULL,
    PROTECT,
)
from django.utils.translation import ugettext_lazy as _

from .events import Event, EventCategory

User = get_user_model()


class Team(models.Model):
    """
    Team model.
    """

    #: Team name
    name = models.CharField(max_length=50)

    #: Event category (as a FK to eventCategory) this team belongs to
    event_category = models.ForeignKey(
        EventCategory,
        related_name="teams",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    #: Team's members
