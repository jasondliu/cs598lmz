import gc, weakref, sys
from weakref import WeakValueDictionary
from .signals import Changed
from .properties import Property, HasProps, MetaHasProps
from . import util

class ColumnDataSource(HasProps):
    """ Maps names of columns to sequences or arrays

    The data is available as a dict-like object, with the keys being the column
    names, and the values being columnar data.

    The data may be specified all at once by passing a dict of columns.

    Alternatively, the columns may be added incrementally, by setting or
    updating the ``ColumnDataSource.data`` attribute.

    Slicing the data object will return a new ``ColumnDataSource`` object
    containing a reference to the original data.

    ColumnDataSource is a subclass of HasProps. It is possible to set
    arbitrary parameters on a ColumnDataSource by setting attributes on it.
    This allows tools to store information about data sources that they may
    need for later use.

    Args:
        data (dict, optional) : a dict where the keys are the column names,
            and the values are the data contained in the column.
