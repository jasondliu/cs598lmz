import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import chain
from operator import attrgetter
from types import MethodType, FunctionType
from weakref import WeakKeyDictionary, WeakValueDictionary

from django.conf import settings
from django.core import signals
from django.db import models
from django.db.models.base import ModelBase
from django.db.models.fields import FieldDoesNotExist
from django.db.models.query import QuerySet
from django.db.models.signals import class_prepared, post_save, pre_save
from django.db.models.sql.constants import LOOKUP_SEP
from django.db.models.sql.where import WhereNode
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _

from polymorphic import PolymorphicModel
from polymorphic.manager import PolymorphicManager
from polymorphic.query import PolymorphicQuerySet
from polymorphic.utils import get_base_polymorphic_model, get_
