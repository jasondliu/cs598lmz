import selectors

from zlib import decompressobj, MAX_WBITS

from . import _exc, utils


def _make_selector():
    """Return a new selector object and the associated object map.

    The object map maps file descriptors to the object that owns them.

    """
    selector = selectors.DefaultSelector()
    objmap = {}

    def map_put(obj, fileobj, events):
        key = selector.get_key(fileobj)
        if key is not None:
            raise ValueError('fd %s already registered' % fileobj)
        selector.register(fileobj, events, data=obj)
        objmap[fileobj.fileno()] = obj

    def map_get(fileobj):
        key = selector.get_key(fileobj)
        if key is None:
            raise ValueError('fd %s not registered' % fileobj)
        return key.data

    def map_del(fileobj):
        key = selector.get_key(fileobj)
        if key is None:
            raise ValueError('fd %
