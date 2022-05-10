import weakref

from . import _pybind_utils as utils
from . import _pybind_state as state
from . import _pybind_types as types
from . import _pybind_core as core

from . import _pybind_core as core
from . import _pybind_types as types
from . import _pybind_state as state
from . import _pybind_utils as utils

from . import _pybind_core as core
from . import _pybind_types as types
from . import _pybind_state as state
from . import _pybind_utils as utils


def _wrap_function(func, wrapper, instance):
    """
    Wrap a function using a wrapper function.

    Parameters
    ----------
    func : callable
        The function to wrap.
    wrapper : callable
        The wrapper function.
    instance : object
        The object to which the function belongs.

    Returns
    -------
    wrapped : callable
        The wrapped function.
    """
