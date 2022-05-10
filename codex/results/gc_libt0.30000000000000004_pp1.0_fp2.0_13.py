import gc, weakref
from collections import defaultdict
from contextlib import contextmanager
from functools import partial
from itertools import chain
from operator import itemgetter
from weakref import WeakKeyDictionary

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.db.models.fields.related import (
    ForeignObjectRel, ForeignObjectRel, ManyToManyRel, ManyToOneRel,
    OneToOneRel,
)
from django.db.models.fields.reverse_related import ForeignObjectRel as ReverseForeignObjectRel
from django.db.models.fields.reverse_related import ManyToManyRel as ReverseManyToManyRel
from django.db.models.fields.reverse_related import ManyToOneRel as ReverseManyToOneRel
from django.db.models.fields.reverse_related import OneToOneRel as ReverseOneToOneRel
from django.db.models.fields.subclassing import SubfieldBase
from django.
