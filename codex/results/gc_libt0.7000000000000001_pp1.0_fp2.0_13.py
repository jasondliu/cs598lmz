import gc, weakref

class WeakMethod:

    def __init__(self, meth):
        self.meth = meth

    def __call__(self, *args, **kw):
        obj = self.meth.im_self
        if obj is None:
            return self.meth(*args, **kw)
        else:
            return self.meth(*args, **kw)


class Signal:

    def __init__(self):
        self.signals = []
        self.signals_weak = weakref.WeakKeyDictionary()

    def connect(self, callback):
        if not callable(callback):
            raise Exception('Callback is not callable')

        if callback not in self.signals:
            self.signals.append(callback)
        else:
            raise Exception('Callback %s is already connected' % str(callback))

    def disconnect(self, callback):
        if not callable(callback):
            raise Exception('Callback is not callable')

        if callback in self.signals:
            self.signals.remove(callback)
        else:

