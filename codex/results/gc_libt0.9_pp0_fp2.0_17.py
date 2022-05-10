import gc, weakref
from collections import namedtuple
from weakref import WeakValueDictionary
from .meshgrid import meshgrid
from .name_generator import NameGen
from .pycompat import unicode
from . import ops
from .utils import is_iterable
from .pycompat import OrderedDict
from . import utils
from . import plot


class DataArray(utils.NDArrayMixin, ops.Func):
    """Implementation of labeled, multi-dimensional arrays

    DataArray is a main data structure for working with multi-dimensional labeled data.
    It is modeled after numpy ndarrays but with richer metadata support and with
    a different API. The API is focused on building new arrays from existing arrays and
    on working with data in the form of labeled dimensions and coordinates.

    Arrays are defined via :meth:`Dataset.variable`, :meth:`Dataset.createVariable`,
    and :meth:`Dataset.createDimension`.

    Create a new array:

    >>> DataArray([1,2,3], attrs={'geom': 'point'
