import gc, weakref
from weakref import WeakKeyDictionary

from numba import types
from numba.typing.templates import (AbstractTemplate, infer, infer_global,
                                    signature, bound_function)
from numba.typing import cffi_utils


class CFuncPtr(types.Opaque):
    """
    A pointer to a C function.
    """
    def __init__(self, args, return_type):
        super(CFuncPtr, self).__init__('CFuncPtr')
        self.args = args
        self.return_type = return_type

    def __eq__(self, other):
        return (super(CFuncPtr, self).__eq__(other) and
                self.args == other.args and
                self.return_type == other.return_type)

    def __hash__(self):
        return hash((self.__class__, self.args, self.return_type))

    def __repr__(self):
        return "%s(%s, %s)" % (self.__class__.__name__
