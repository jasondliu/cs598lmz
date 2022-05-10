import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import warnings

__all__ = ['get_config']

def get_config():
    """Return a dictionary of configuration parameters.

    When called from the main Python interpreter, this function returns the
    configuration parameters used to compile the interpreter.  When called from
    a Python interpreter embedded in a different application, this function
    returns the configuration parameters that were used to compile the
    application.
    """
    from _sysconfigdata import build_time_vars
    from _sysconfigdata import makefile_vars
    from _sysconfigdata import configure_vars
    from _sysconfigdata import get_paths
    from _sysconfigdata import get_platform
    from _sysconfigdata import get_scheme_names

    config = {}
    config.update(build_time_vars)
    config.update(makefile_vars)
    config.update(configure_vars)
    config.update(get_paths(get_platform(), get_scheme_names()))
