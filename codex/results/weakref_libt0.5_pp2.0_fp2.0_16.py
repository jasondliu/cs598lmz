import weakref
import re

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm.session import object_session

from .utils import *
from . import log

__all__ = ['Model', 'Table', 'Column', 'ForeignKey', 'OneToMany', 'ManyToOne',
           'OneToOne', 'ManyToMany', 'ManyToManyCollection', 'session',
           'transaction', 'flush', 'commit', 'rollback', 'create_all',
           'drop_all', 'bind']

def _get_decl_class(cls):
    if hasattr(cls, '__declare_last__') and cls.__declare_last__:
        return cls
    else:
        for c in cls.__mro__:
            if hasattr(c, '__table__'):
                return c

def _get_mapper(cls):
    return object_session(cls).mapper(cls)

def _get_column
