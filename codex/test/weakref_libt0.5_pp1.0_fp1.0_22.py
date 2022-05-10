import weakref

import numpy as np

from . import _core
from . import _util

class _HDF5Object(object):
    """
    Base class for HDF5 objects.

    This class provides common functionality for all HDF5 objects, such as
    reference counting, weak references, and garbage collection.
    """

    #: The number of references to this object.
    _refcnt = None

    def __init__(self):
        """
        Initialize a new HDF5 object.
        """
        # Create a weak reference to the object.
        self._weakref = weakref.ref(self, self._weak_callback)

        # Increment the reference count.
        self._refcnt = 1

    def __del__(self):
        """
        Delete an HDF5 object.
        """
        # Decrement the reference count.
        self._refcnt -= 1

        # If the reference count is zero, delete the object.
        if self._refcnt == 0:
            self._delete()

