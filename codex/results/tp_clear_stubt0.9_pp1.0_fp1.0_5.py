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

for i in range(1000):
    globals()[str(i)] = i

gc.collect()

func()
'''

class AppTestWeakRef: 
    spaceconfig = dict(usemodules=['_weakref'])

    def setup_class(cls):
        global OptionError
        from _weakref import OptionError

    def test_callback(self): 
        i = 0 
        class Foo: 
            global i 
            def __del__(self): 
                i += 1 
        def foo():
            pass 
        f = Foo() 
        x = weakref.ref(f, foo) 
        del f 
        gc.collect() 
        assert i == 1 
        x() 

    def test_callback_exc(self): 
        i = 0 
        class Foo: 
            global i 
            def __del__(self): 
                raise TypeError 
        def foo():
            i += 1 
        f = Foo() 
        x = weak
