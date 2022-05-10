import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

class _Evaluator(object):
    __slots__ = ('eval', 'globals', 'locals')
    
    def __init__(self, eval, globals, locals):
        self.eval = eval
        self.globals = globals
        self.locals = locals
    
    def __call__(self, source):
        return self.eval(source, self.globals, self.locals)
    
    def __repr__(self):
        return '<%s at 0x%x>' % (self.__class__.__name__, id(self))

def _make_evaluator(eval, globals, locals):
    return _Evaluator(eval, globals, locals)

def _make_evaluator_from_frame(frame):
    return _Evaluator(frame.f_eval, frame.f_globals, frame.f_locals)

