import weakref

from . import _ffi as ffi, _lib as lib
from . import _util
from . import _cffi_backend


class _CDataMeta(type):
    """Metaclass for _CData"""

    def __new__(cls, name, bases, dct):
        if name == '_CData':
            return type.__new__(cls, name, bases, dct)
        if '_type_' in dct:
            raise TypeError("_CData subclass cannot define _type_")
        if '_subtype_' in dct:
            raise TypeError("_CData subclass cannot define _subtype_")
        if '_subarray_type_' in dct:
            raise TypeError("_CData subclass cannot define _subarray_type_")
        if '_subarray_shape_' in dct:
            raise TypeError("_CData subclass cannot define _subarray_shape_")
