import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

class Hoge(object):
    def __init__(self):
        self.on_tick = FUNTYPE(self.on_tick)

    def on_tick(self, user_data, tick):
        print tick


h = Hoge()
DLL.begin(h.on_tick, ctypes.pointer(h))
</code>

