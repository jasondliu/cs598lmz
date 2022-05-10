import ctypes
ctypes.cast(0, ctypes.py_object)

#
# __import__(name, globals={}, locals={}, fromlist=[], level=-1)
#
# name is a string.
#
# globals is a dictionary.
#
# locals is another dictionary.
#
# fromlist is a list of strings.
#
# level is an integer.
#
# fromlist is a list of strings. Each is a name that can be imported from the
# module.
#
# level is an integer. It's the relative position of the module in the
# package hierarchy.
#

#
# __import__(name, globals={}, locals={}, fromlist=[], level=-1)
#

import sys

def import_module(name, globals=None, locals=None, fromlist=None, level=-1):
    """
    Import and return the module. The 'globals' argument is used to infer
    where the module is relative to the caller's module. The 'locals'
    argument is ignored. The 'fromlist' argument specifies what should exist
    as attributes
