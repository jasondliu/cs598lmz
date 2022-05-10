import weakref

from . import _core
from . import _util

class _Base(object):
    """Base class for all objects in the library.

    This class is used to provide common functionality for all objects
    in the library.

    """

    def __init__(self, handle):
        """Initialize a new object.

        This constructor is not meant to be called directly by users of
        the library.

        """
        self._handle = handle

    def __del__(self):
        """Release the object's resources.

        This method is called when the object is about to be destroyed.
        It will release the object's handle so that the underlying
        library can free the associated resources.

        """
        if self._handle is not None:
            _core.lib.git_object_free(self._handle)
            self._handle = None

    @property
    def id(self):
        """Read-only attribute to access the object's id.

        This is the unique identifier for the object.

        """
        return _util.hex_to_hash(
            _core.ffi.
