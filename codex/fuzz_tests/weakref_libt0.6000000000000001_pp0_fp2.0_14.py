import weakref

import numpy as np

from . import utils


class Data:
    """
    Abstract base class for 1D and 3D data.

    :Attributes:

        * `data` : numpy.ndarray
            The data.

        * `name` : string
            The name of the data

        * `unit` : string
            The unit of the data

        * `unit_type` : string
            The type of the unit, e.g. 'frequency'

        * `unit_prefix` : string
            The prefix of the unit, e.g. 'milli'

        * `spacing` : float or None
            The spacing in the data.

        * `origin` : float or None
            The origin in the data.

        * `data_type` : str
            The type of the data, e.g. 'real'

        * `shape` : tuple
            The shape of the data

        * `ndim` : int
            The number of dimensions

        * `size` : int
            The total number of points

        * `is_complex` : bool
