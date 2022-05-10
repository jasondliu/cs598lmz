import gc, weakref, time

class WeakCallback:
    def __init__(self, callback):
        self._callback = callback
        self._objid = id(callback.__self__)

    def __eq__(self, other):
        return self._objid == other._objid

    def __call__(self, *args, **kwds):
        self._callback(*args, **kwds)

    def __hash__(self):
        return self._objid


class WeakMethod:
    def __init__(self, method):
        self._method = method.im_func
        self._objid = id(method.im_self)

    def __eq__(self, other):
        return self._objid == other._objid

    def __call__(self, *args, **kwds):
        return self._method(*args, **kwds)

    def __hash__(self):
        return self._objid


class Callback:
    def __init__(self, callback_list, callback):
        if hasattr(callback, 'im_func'):

