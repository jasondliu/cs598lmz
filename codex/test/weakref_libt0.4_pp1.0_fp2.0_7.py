import weakref

from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField

from .managers import UserManager


# A few helper functions for common logic between User and AnonymousUser.
def _user_get_all_permissions(user, obj):
    permissions = set()
    for backend in auth.get_backends():
        if hasattr(backend, "get_all_permissions"):
            permissions.update(backend.get_all_permissions(user, obj))
    return permissions


def _user_has_perm(user, perm, obj):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
