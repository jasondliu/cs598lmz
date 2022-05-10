import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# Import the builtin modules.
import __builtin__
import __main__

# Import the warnings module, but do not override the built-in one so that
# we can use the warnings from this module to warn about deprecated features
# of the built-in warnings module.
import warnings as _warnings

# Import the _warnings module.  This is the implementation of the warnings
# module; we store a reference to it in this module so that we can add a
# filter in warnings.py to raise an error if a warning is triggered in the
# _warnings module.
import _warnings

# Import the _weakrefset module.
import _weakrefset

# Import the abc module.
import abc

# Import the copyreg module.
import copyreg

# Import the genericpath, ntpath, os2emxpath, and macpath modules.
import genericpath
import ntpath
import os2emxpath
