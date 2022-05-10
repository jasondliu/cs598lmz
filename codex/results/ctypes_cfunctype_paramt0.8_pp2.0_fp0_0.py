import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def _create_callback(funstr):
    """
    Create callback loop using eval
    """
    _callback_functype = FUNTYPE(funstr)
    def _callback():
        return _callback_functype()
    return _callback

class Callback(object):
    """
    Object that represents the callback provided
    by the user
    """
    def __init__(self, parent, funstr):
        self.parent = parent
        self.funstr = funstr
        self._callback = _create_callback(self.funstr)

    def __call__(self):
        # print "Calling callback..."
        self._callback()
        return False

class Component(object):
    """
    Component Object class
    """
    def __init__(self, component, callback, **kwargs):
        self.comp = component
        self.parent = None
        self.is_top_level = False
        self.callback = Callback(self, callback)
        self.comp.callback = self.callback

    def update(self):
       
