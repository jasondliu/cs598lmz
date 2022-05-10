import weakref
import logging
import pickle

from datetime import datetime

from django.db import models, transaction
from django.db.models.loading import get_model


class DjangoModel(object):
    model_class = None
    _id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @classmethod
    def find(cls, id):
        values = cls.model_class.objects.values('id', 'data').get(id=id)
        instance = cls.model_class(id=values['id'], data=values['data'])
        return instance

    @classmethod
    def find_all(cls):
        values = list(cls.model_class.objects.values('id', 'data'))
