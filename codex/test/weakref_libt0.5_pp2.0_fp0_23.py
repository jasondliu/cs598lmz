import weakref

from . import util

from .util import (
    auto_str,
    auto_repr,
)

from . import (
    const,
    errors,
    types,
)


@auto_str
@auto_repr
class Object(object):
    """
    The base class for all objects in the library.

    This class is also used for objects that are not directly
    exposed to the user, but are used internally.

    All objects have a parent, which is the object that
    contains them. For example, a :class:`~.datatypes.DataType`
    object has a parent that is a :class:`~.datatypes.Structure` object.
    """

