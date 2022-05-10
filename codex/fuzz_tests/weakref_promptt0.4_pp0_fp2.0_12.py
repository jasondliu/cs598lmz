import weakref
# Test weakref.ref(x) where x is a subclass of a built-in type

class MyInt(int):
    pass

class MyList(list):
    pass

class MyDict(dict):
    pass

class MyStr(str):
    pass

class MyTuple(tuple):
    pass

def check(x):
    r = weakref.ref(x)
    x2 = r()
    print(type(x), type(x2))
    assert type(x) is type(x2)

check(MyInt())
check(MyList())
check(MyDict())
check(MyStr())
check(MyTuple())
