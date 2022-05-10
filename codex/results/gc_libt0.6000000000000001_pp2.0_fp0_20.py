import gc, weakref

from .base import DbObject
from . import utils
from . import dialects

logger = logging.getLogger("dbobj")

class DbObjectMeta(type):
    def _register_class(cls, name, bases, attrs):
        if '__db_name__' in attrs:
            name = attrs['__db_name__']
        else:
            name = cls.__name__
        if name in DbObject.__subclasses__:
            return
        DbObject.__subclasses__[name] = cls
        cls.__db_name__ = name
        cls.__db_fields__ = []
        cls.__db_indexes__ = []
        cls.__db_relations__ = []
        cls.__db_reverse_relations__ = {}
        fields = []
        for base in bases:
            fields.extend(base.__db_fields__)
        for attr_name, attr in attrs.items():
            if attr_name.startswith("
