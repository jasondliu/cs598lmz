import _struct

from . import (
    constants,
    exceptions,
    utils,
)


class _LazyProperty(object):
    """
    A descriptor which caches the result of the property.
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class _LazyClassProperty(_LazyProperty):
    """
    A descriptor which caches the result of the class property.
    """
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(owner)
        setattr(owner, self.name, value)
        return value


class _LazyStaticProperty(_LazyProperty):
    """
    A descriptor which caches the result of the static property
