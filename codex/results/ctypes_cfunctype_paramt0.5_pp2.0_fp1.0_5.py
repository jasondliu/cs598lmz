import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class My_Callback(object):
    def __init__(self, callback):
        self.callback = callback
    def __call__(self, *args):
        return self.callback(*args)

class My_Callback2(object):
    def __init__(self, callback):
        self.callback = callback
    def __call__(self, *args):
        return self.callback(*args)


class My_Callback3(object):
    def __init__(self, callback):
        self.callback = callback
    def __call__(self, *args):
        return self.callback(*args)


class My_Callback4(object):
    def __init__(self, callback):
        self.callback = callback
    def __call__(self, *args):
        return self.callback(*args)


class My_Callback5(object):
    def __init__(self, callback):
        self.callback = callback
    def __call__(self, *args):
        return self.callback(*args)


class My_Callback6(object):
