import gc, weakref
from . import settings
from . import errors
from . import events
from . import events_impl
from . import utils
from . import logging

from . import _lib
from . import _lib_impl

from ._lib import g_log_set_handler_full

from ctypes import c_char_p, c_int, c_void_p
from ctypes import POINTER, byref, cast

__all__ = ['Application', 'ApplicationClass', 'ApplicationFlags']

_log = logging.getLogger('Application')


class ApplicationFlags(utils.Flags):
    """Flags used to construct an Application.

    Flags should be combined using the bitwise OR operator.

    .. seealso:: the `Application constructor
       <http://developer.gnome.org/gobject/stable/gobject-The-Base-Object-Type.html#GApplicationFlags>`_
    """

    FLAGS = [
        ('FLAGS_NONE', _lib.G_APPLICATION_FLAGS_NONE),
        ('IS_SERVICE', _lib.G_APPLIC
