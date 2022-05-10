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

from .dataclasses import (
    field,
    MISSING,
    Field,
    _process_class,
    _is_dataclass,
    _get_field_type,
    _get_fields,
    _post_init_copy,
    make_dataclass,
    replace,
    asdict,
    astuple,
    is_dataclass,
    fields,
    field_names,
    field_values,
    _is_field,
    _MISSING_TYPE,
    _M
