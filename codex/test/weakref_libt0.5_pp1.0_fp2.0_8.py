import weakref
from collections import defaultdict
from functools import wraps

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet
from django.utils.importlib import import_module

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

from .models import Rating, SimilarItem, SimilarUser
from .signals import post_rate, pre_rate


# The maximum number of similar items to return for a given item
SIMILAR_LIMIT = getattr(settings, 'SIMILARITY_LIMIT', 10)

# The maximum number of similar users to return for a given user
SIMILAR_USER_LIMIT = getattr(settings, 'SIMILARITY_USER_LIMIT', 10)

# The maximum number of ratings to use when calculating similarity
SIMILAR_MAX_RATINGS = getattr(settings, 'SIMILARITY_MAX_RATINGS', 200)

# The minimum
