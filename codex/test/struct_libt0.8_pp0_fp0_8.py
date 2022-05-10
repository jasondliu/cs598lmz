import _struct

# Select the correct 64bit unpack function.
if sys.version_info.major >= 3 and sys.version_info.minor >= 2:
    unpack = _struct.unpack_from
else:
    unpack = _struct.unpack

class NDArray(object):
    """A simple container for numpy arrays.
    """
    def __init__(self, array, context, grad_stype=None, stype='default'):
        """Initialize a new array.
        """
        if not isinstance(array, np.ndarray):
            array = np.array(array)

        if context is not None:
            if array.dtype is np.dtype('object'):
                raise TypeError("NDArray does not support dtype=object")

        self._stype = stype
        self._array = array
        self._context = context

    @property
    def shape(self):
        """Get the shape of the array.
        """
        return self._array.shape

