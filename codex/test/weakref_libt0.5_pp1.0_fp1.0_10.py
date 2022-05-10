import weakref

import numpy as np

from . import _base


class Coordinate(_base.Coordinate):
    """
    A coordinate class for the `DataArray` class.
    """

    def __init__(self, name, data, attrs=None, encoding=None, fastpath=False):
        """
        Create a Coordinate object.

        Parameters
        ----------
        name : str
            Name of this coordinate.
        data : array_like
            Values for this coordinate.
        attrs : dict_like, optional
            Attributes to assign to the new coordinate. By default, an empty
            attribute dictionary is initialized.
        encoding : dict_like, optional
            Dictionary specifying how to encode this array's data into a
            serialized format like netCDF4. Currently used keys (for netCDF)
            include '_FillValue', 'scale_factor', 'add_offset' and 'dtype'.
        fastpath : bool, optional
            Don't parse data for encoding or coordinate properties (e.g.,
            units).
        """
