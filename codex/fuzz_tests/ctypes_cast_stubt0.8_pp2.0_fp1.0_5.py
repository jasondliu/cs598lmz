import ctypes
ctypes.cast(0, ctypes.py_object)

import sys, ctypes
from ctypes import pythonapi, py_object, c_long, c_char
from types import ModuleType

def inject_into_dict(d, key, value):
    """
    Inject a key, value pair into a dictionary, even if that dictionary is
    read-only (builtins/__builtin__)

    Code from http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/#fn-2
    """
    pythonapi.PyDict_SetItem(c_long(id(d)),
                             py_object(key), py_object(value))

def make_module(name, doc=None):
    """
    Make a new module type, suitable for injection into sys.modules

    We're not supposed to create new modules, so we have to trick ctypes.
    """
    m = ModuleType(name, doc)
    m.__loader__ = None
    return m

def install_fake(name, fake, real=None):

