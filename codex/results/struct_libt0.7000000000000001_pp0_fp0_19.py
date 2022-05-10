import _struct

from . import _compat
from . import _types

from .constants import *
from .internal import *
from .utils import *

from . import _funcs

from .exceptions import *
from .exceptions.notify import *


__all__ = ["InitError",
           "QuitError",
           "get_init", "get_quit",
           "init", "quit",
           "get_version",
           "was_init",
           "get_error", "clear_error",
           "get_error_string", "get_error_state",
           "set_error", "set_error_state",
           "get_error_name",
           ] + _funcs.__all__


_py_to_al_error = {0: "NO_ERROR",
                   1: "INVALID_NAME",
                   2: "INVALID_ENUM",
                   3: "INVALID_VALUE",
                   4: "INVALID_OPERATION",
                   5: "OUT_OF_MEMORY",
                   6:
