import gc, weakref
import operator
from datetime import datetime, timedelta, MAXYEAR

from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q
from django.db.models.sql.datastructures import Join
from django.db.models.sql.query import DeleteQuery, UpdateQuery
from django.db.models.sql.where import Constraint, ExtraWhere
from django.utils.functional import Promise

from djangotricks import functools, utils
from djangotricks.caching import model_attributes
from djangotricks.caching.attributes import get_attribute_cache, model_attr_name
from djangotricks.caching.attributes import ALL_ACCESS_TYPE_ID
from djangotricks.caching.generic import model_str_to_model, get_model
from djangotricks.caching.lookup import prepare_lookup_value


class QuerySetWithCache(QuerySet):
    CACHE_TTL = 0  # caching time in seconds
