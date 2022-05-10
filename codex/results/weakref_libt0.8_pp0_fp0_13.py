import weakref
from datetime import datetime
from functools import reduce

from django.db import models, transaction


prefix = "cocoon.sqlalchemy."
ref_key = prefix + "ref"
version_key = prefix + "version"


def get_version(object):
    return object.__dict__.get(version_key)


def set_version(object, version):
    object.__dict__[version_key] = version


def get_ref(object):
    return object.__dict__.get(ref_key)


def set_ref(object, ref):
    object.__dict__[ref_key] = ref


class DynamicWrapper(object):

    def __init__(self, model, query):
        self._environ = query._environ
        self._query = query
        self._model = model
        self._mappers = {}

    def __getattr__(self, item):
        if item not in self._mappers:
            mapper = self._model.__mapper__
            self._mappers[item
