import weakref

from .constants import *
from .exceptions import *
from .utils import *

__all__ = ('Base', 'BaseMeta', 'BaseDict', 'BaseDictMeta', 'BaseList', 'BaseListMeta')


class BaseMeta(type):
    """
    Base class for all metaclasses.
    """

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace)
        cls.__slots__ = tuple(namespace.get('__slots__', ()))
        return cls


class Base(metaclass=BaseMeta):
    """
    Base class for all classes.
    """

    __slots__ = ()


class BaseDictMeta(BaseMeta, dict):
    """
    Base class for all dict metaclasses.
    """

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace)
