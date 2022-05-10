fn = lambda: None
# Test fn.__code__

class C:
    def meth(self):
        print('meth')

o = C()
o.meth.__code__

# Test fn.__defaults__
def f(a,b,c=3,d=4):
    print(a,b,c,d)

f.__defaults__

# Test fn.__globals__
def f():
    global x
    x = 1

x = 0
f.__globals__['x']

def f():
    print(y)

y = 1
f.__globals__['y']

# Test fn.__closure__
def f(x):
    def g():
        print(x)
    return g

f(1).__closure__

def f():
    x = 1
    def g(x=x):
        print(x)
    return g

f()(5).__closure__

# Test fn.__annotations__
def f(a:'A', b:'B') -> 'C':
    pass

