import weakref

class WeakConnectionsMixin(object):
    def __init__(self):
        super(WeakConnectionsMixin, self).__init__()
        self.__dict__["_weakConnections"] = weakref.WeakKeyDictionary()

    def _get_signal_map(self):
        klass = self.__class__
        try:
            weak = self._weakConnections[klass]
        except KeyError:
            weak = self._weakConnections[klass] = weakref.WeakKeyDictionary()

        return weak

    def _connect(self, signal, func, data=None):
        try:
            func = func.__func__
        except AttributeError: pass

        data = data or {}
        weak = self._get_signal_map()
        weak.setdefault(signal, []).append((func, data))

    def _connect_once(self, signal, func):
        self._connect(signal, func, data={"once": True})

    def _emit(self, signal, *args, **kwargs):
