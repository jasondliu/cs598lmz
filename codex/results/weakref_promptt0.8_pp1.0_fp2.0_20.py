import weakref
# Test weakref.ref() 

class C:
    __slots__ = ('x', 'y', 'z')

def callback(r, d):
    print("callback", r, d)

def test(o):
    wr = weakref.ref(o, callback)
    wwr = weakref.WeakValueDictionary({'key': o})
    print(wwr)
    del o
    print(wr())
    print(wwr)
    print(wwr.get('key'))

a = C()
a.x = 10
a.y = 20
a.z = 30

test(a)

a = list(range(10))

test(a)

a = tuple(range(10))

test(a)

# Test weakref.ref() with a subclass of a builtin, with and without slots

class A:
    __slots__ = ('x',)

class B(A):
    __slots__ = ('x', 'y')

class C(tuple):
    pass

class D(C):
   
