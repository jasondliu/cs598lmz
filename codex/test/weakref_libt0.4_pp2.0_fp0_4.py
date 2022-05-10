import weakref

from . import _cffi_backend
from . import _cffi_errors
from . import _cffi_opcode
from . import _cffi_utils
from . import _embedding
from . import _types
from . import _cdata
from . import _cdataobj


# ____________________________________________________________
#
#  Support for the 'cdef()' function.  It is implemented as a
#  class with an instance method, so that it can be used as a
#  decorator.

class _CDefError(Exception):
    def __init__(self, message, filename, lineno):
        self.message = message
        self.filename = filename
        self.lineno = lineno

    def __str__(self):
        return '%s:%d: %s' % (self.filename, self.lineno, self.message)


class _CDefBase(object):
    def __init__(self, ctx):
        self.ctx = ctx

