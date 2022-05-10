import weakref

from . import _libsodium
from . import _ffi
from . import _utils
from . import exceptions


class SodiumError(exceptions.SodiumError):
    """
    Exception raised when libsodium encounters an error.
    """


class Sodium(object):
    """
    This class is a wrapper for the libsodium library.

    It contains all the functionality of libsodium and is the only class you
    should need to import from pysodium.

    Note that this class is a singleton, so you should never need to instantiate
    it. Instead, you should import it directly from pysodium:

        >>> from pysodium import sodium
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Sodium, cls).__new__(cls)
        return cls._instance

