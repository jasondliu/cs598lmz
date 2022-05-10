import weakref

import numpy as np

from . import _base
from . import _util
from . import _data_obj


class _Data(_base.Data):
    """
    Base class for all data types.

    This class is not intended to be used directly.
    """

    def __init__(self, data, name=None, label=None, parent=None, info=None,
                 plotter=None, group=None, attrs=None):
        """
        Parameters
        ----------
        data : array_like
            The data to be stored in the Data object.
        name : str, optional
            The name of the data.
        label : str, optional
            The label to be used when plotting the data.
        parent : Data or None, optional
            The parent of this data.
        info : dict, optional
            A dictionary to store information about this data.
        plotter : Plotter, optional
            A Plotter to be used for plotting operations.
        group : h5py.Group, optional
            An HDF5 group object to store the data in.
        att
