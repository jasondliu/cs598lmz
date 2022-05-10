import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

class LispParser(object):
    import re
    SPLITTER = re.compile(r'(\(|\)|'+re.escape(NAME_CHARS)+'*|\s+)', re.S)

    def __init__(self):
        self.interpreter = Interpreter()
        self.interpreter.locals['eval'] = self.interpreter.eval
        self.interpreter.locals['_'] = None

    def eval(self, program):
        a = self.parse(program)
        return self.interpreter._eval(a[1])

    def parse(self, program):
        a = self.SPLITTER.split(program)
        del a[0]
        a = [(lambda x: {'(': '-L', ')': '-R'}.get(x, x))(x) for x in a]
        if len(a) >= 3 and a[1] == '-L' and
