import weakref

from . import _cffi_backend
from . import _cffi_errors
from . import _cffi_utils
from . import _embedding
from . import _typeof

_cffi_backend.init_types(rffi.LONG, rffi.ULONG)


class _CDataMeta(type):
    """Metaclass for _CData.  This is the class of all CData objects."""

    def __new__(cls, name, bases, dct):
        if name == '_CData':
            return type.__new__(cls, name, bases, dct)
        if '_type_' not in dct:
            raise TypeError("class %s lacks a _type_ attribute" % name)
        type = dct['_type_']
        if not isinstance(type, _cffi_backend.CType):
            raise TypeError("class %s has a _type_ attribute which is not "
                            "a CType instance" % name)
        if not type.is_
