import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()
try:
    gc.collect()
except AttributeError: pass
''',
)

#XXX Segfaults if optlevel>1
if sys.version_info >= (2, 7):
    try:
        if sys.platform == 'darwin':
            raise Exception()
        code = compile('import x', '?', 'exec')
        globals()
        eval(code, {})
    except (ImportError, SyntaxError):
        pass
    else:
        if sys.version_info < (3, 0):
            exec 'x=x'

        testcode_check_stack_effect('''
