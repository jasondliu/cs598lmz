import weakref

import numpy as np

from . import utils
from .utils import (
    get_repr,
    get_repr_tuple,
    get_repr_list,
    get_repr_dict,
    get_repr_namedtuple,
    get_repr_numpy,
    get_repr_set,
    get_repr_frozenset,
    get_repr_weakref,
    get_repr_weakproxy,
    get_repr_object,
    get_repr_method,
    get_repr_callable,
    get_repr_function,
    get_repr_class,
    get_repr_module,
    get_repr_instance,
    get_repr_generator,
    get_repr_coroutine,
    get_repr_async_generator,
    get_repr_async_coroutine,
)

from . import typemap


class ObjectRepr(object):
    """
    This class is a
