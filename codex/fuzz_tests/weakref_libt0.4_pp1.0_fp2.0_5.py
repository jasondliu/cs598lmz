import weakref

from . import _lib
from . import _ffi
from . import _api

from . import _util
from . import _errors
from . import _compat

from . import _errors
from . import _util


class _Context(object):
    '''
    This is the base class for all contexts.
    '''

    def __init__(self, ctx):
        self._ctx = ctx

    def __del__(self):
        self._destroy()

    def _destroy(self):
        if self._ctx:
            _lib.zmq_ctx_destroy(self._ctx)
            self._ctx = None

    def term(self):
        '''
        Terminate the context.

        This is a non-blocking operation. The context will be terminated
        when all sockets associated with it have been closed.
        '''
        if self._ctx:
            _lib.zmq_ctx_term(self._ctx)
            self._ctx = None

    def term_endpoint(self, addr):
        '''
        Terminate a
