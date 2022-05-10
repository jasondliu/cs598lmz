import weakref
# Test weakref.ref() with a function.

class Foo:
    pass

def func ():
    pass

def func2 ():
    pass

def func3 ():
    pass

def func4 ():
    pass

def func5 ():
    pass

foo = Foo()
func2 = func

def func6 ():
    func3 = func
    ref1 = weakref.ref(func)
    ref2 = weakref.ref(func2)
    ref3 = weakref.ref(func3)
    ref4 = weakref.ref(foo)
    ref5 = weakref.ref(func4)
    ref6 = weakref.ref(func5)
    del func
    del func2
    del func3
    del foo
    del func4
    del func5
    try:
        ref1()
        ref2()
        ref3()
        ref4()
        ref5()
        ref6()
    except ReferenceError:
        pass
    else:
        print('ReferenceError not raised')

func6()
