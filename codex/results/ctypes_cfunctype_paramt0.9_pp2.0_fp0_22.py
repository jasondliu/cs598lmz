import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class Dispatcher:
    "provides simple callback registry and dispatcher"
    def __init__(self):
        self._cbs = set()
    def register(self, callb):
        if callable(callb):
            self._cbs.add(callb)
        else:
            cbfun = getattr(callb, _cbattrname, None)
            if cbfun is None:
                cbfun = FUNTYPE(callb)
                setattr(callb, _cbattrname, cbfun)
            self._cbs.add(cbfun)
    def unregister(self, callb):
        self._cbs.remove(callb)
    def dispatch(self, *args, **kwargs):
        for cb in self._cbs:
            cb(*args, **kwargs)
</code>
See it in action:
<code>&gt;&gt;&gt; cls = Dispatcher
&gt;&gt;&gt; d = cls()
&gt;&gt;&gt; d
