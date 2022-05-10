import weakref

from . import base
from . import exceptions
from . import fields
from . import utils

logger = logging.getLogger(__name__)


class Model(base.Model):
    _db = None
    _collection = None

    @classmethod
    def _get_collection(cls):
        if cls._collection is None:
            cls._collection = cls._db[cls.__name__]
        return cls._collection

    @classmethod
    def _get_pk(cls):
        return cls._get_collection().create_index([('_id', 1)], unique=True)

    @classmethod
    def _get_indexes(cls):
        indexes = []
        for name, field in cls._fields.items():
            if isinstance(field, fields.Index):
                indexes.append((name, 1))
        return cls._get_collection().create_index(indexes, unique=True)

    @classmethod
    def _get_indexes_async(cls):
        return async
