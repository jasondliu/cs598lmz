import _struct
import _ctypes
import ctypes
import ctypes.util

import warnings as std_warnings

class SimpleCData(object):
    """Base class for instances of C simple type arguments."""
    _type_ = 'B'
    _subtype_ = None # a SimpleType subclass
    _length_ = None # the length (of the _subtype_, if any)
    _is_pointer_ = False
    _is_array_ = False
    _is_string_ = False
    _is_unicode_ = False
    _is_raw_ = False
    
    # XXX This assumes that no one will make an instance of this type, or of
    # a type derived from this type, without having set _type_.  I think
    # that's only reachable from C _testcapi.
    __slots__ = ()

    def __repr__(self):
        if self._type_ == 'z':
            content = ctypes.cast(self, ctypes.c_char_p).value
