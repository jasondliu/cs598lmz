import weakref
# Test weakref.ref(x)
def test1():
    x = [1, 2]
    a = weakref.ref(x)
    x = None
test1()
# Test weakref.ref(x, xxx)
def test2():
    x = [1, 2]
    a = weakref.ref(x, lambda x: None)
    x = None
test2()
# Test weakref.ref(x, xxx)
def test3():
    x = [1, 2]
    a = weakref.ref(x, lambda x: None)
    x = None
test3()
# Test weakref.ref(x, xxx)
def test4():
    x = [1, 2]
    a = weakref.ref(x, lambda x: None)
    x = None
test4()
# Test weakref.ref(x, xxx)
def test5():
    x = [1, 2]
    a = weakref.ref(x, lambda x: None)
    x = None
test5()
# Test weakref.ref(x,
