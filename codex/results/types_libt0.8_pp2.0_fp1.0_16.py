import types
types.FunctionType

def f(x):
    x(3)

f(lambda x: print(x))

f(lambda x: x)

def g():
    pass

g()

class C:
    pass

C()

x = C()
x

x.__class__

y = f(lambda x: x)
y

y.__class__

x.__class__

def f(x):
    return x(3)

f(lambda x: print(x))

def g(x):
    return x()

g(lambda: 3)

def h():
    return 3

g(h)

def h():
    def k():
        return 4
    return k

h()()

h()

h

h()

# Does this work?
z = h()

# Does this work?
z()

# Does this work?
f = h()

f()

# A lambda can sometimes serve as a quick way to create a new function.
g = lambda
