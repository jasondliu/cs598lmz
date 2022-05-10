import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(1)

def f(x, y):
    print(x, y)
    print(g)

def g():
    print('g')

def h(x):
    print('h')
    return x

def k(x):
    print('k')
    return x

def m(x):
    print('m')
    return x

class A:
    def __init__(self, x):
        self.x = x
        self.f = f
        self.a = [A(x) for x in range(3)]
        #self.b = [B(x) for x in range(3)]

    def __del__(self):
        print('__del__', self.x)

#class B:
#    def __init__(self, x):
#        self.x = x
#        self.b = [B(x) for x in range(3)]
#
#    def __del__(self):
#        print('__del__', self.x)

class C:
    def __
