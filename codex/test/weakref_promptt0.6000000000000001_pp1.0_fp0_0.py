import weakref
# Test weakref.ref() to see if it creates a weak reference.
try:
    weakref.ref
except AttributeError:
    from .weakref_backports import ref
else:
    del weakref

from .abc import (
    ABC,
    abstractmethod,
    abstractproperty,
    abstractclassmethod,
    abstractstaticmethod,
)

from .classproperty import classproperty

from .cached_property import cached_property

from .dataclass import dataclass

from .dataclass_json import dataclass_json

