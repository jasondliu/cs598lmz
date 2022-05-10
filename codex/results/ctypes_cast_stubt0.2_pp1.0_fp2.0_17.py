import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented functionality.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

# ___________________________________________________________________________
# Functions

def is_string(obj):
    """Return True if obj is a string, False otherwise."""
    return isinstance(obj, basestring)

def is_sequence(obj):
    """Return True if obj is a sequence, False otherwise."""
    return isinstance(obj, collections.Sequence)

def is_mapping(obj):
    """Return True if obj is a mapping, False otherwise."""
    return isinstance(obj, collections.Mapping)

def is_number(obj):
    """Return True if obj
