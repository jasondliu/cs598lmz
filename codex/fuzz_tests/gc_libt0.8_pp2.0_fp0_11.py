import gc, weakref
from . import importer
import multiprocessing.queues
from .wrapper import ProxyWrapper
from .utils import get_object_id


class Proxy(object):
    """
    Proxy class

    Internal class that represents a proxy to an object and
    manages its lifetime.
    """
    def __init__(self, obj, ref=None):
        """
        Create new proxy

        Parameters
        ----------
        obj : object
            An object to be proxied.
        ref : weakref
            If provided, proxy will use the given reference instead
            of creating a new one.
        """
        # Check if reference is weak
        if ref is None or not isinstance(ref, weakref.ref):
            # Create a reference to object
            self._ref = weakref.ref(obj, self._on_object_deleted)
        else:
            self._ref = ref

        # Increase object reference count
        obj.__imp_ref_count += 1

        # Get objects info
        self._info = ProxyWrapper.get_info(obj)

    def _on_
