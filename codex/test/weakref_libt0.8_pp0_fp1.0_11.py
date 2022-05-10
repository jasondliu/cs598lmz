import weakref
import logging

from . import _proxy, _core, _lib
from .utils import _proplem

log = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
#
class _float_proxy(_proxy._proxy):
    """Proxy to a float value.
    """

    # --------------------------------------------------------------------------
    #
    def __init__(self, index, _obj):
        """Create a new float proxy.

        Arguments:
          index (int): index of the value
          _obj (:class:`~radical.ensemblemd.ReverseProxy`): ReverseProxy to the
          actual object.
        """
        self._index = index
        self._obj = _obj
        self._name = "<float %d>" % index

        # register callback
        _obj._callbacks[index] = self


    # --------------------------------------------------------------------------
    #
    def __del__(self):
        """A cleanup method for the object.
        """

