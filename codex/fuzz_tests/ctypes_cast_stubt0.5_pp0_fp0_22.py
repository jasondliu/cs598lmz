import ctypes
ctypes.cast(1, ctypes.py_object)

# Storing a reference to a function
def foo(x):
    print 'executing foo(%s)' % (x,)

class A(object):
    pass

a = A()
a.foo = foo
x = 10
a.foo(x)

# Storing a reference to a class
def bar(x):
    print 'executing bar(%s)' % (x,)

class A(object):
    pass

a = A()
a.bar = bar
x = 10
a.bar(x)

# Storing a reference to an instance method
def baz(x):
    print 'executing baz(%s)' % (x,)

class A(object):
    pass

a = A()
a.baz = baz
x = 10
a.baz(x)

# Storing a reference to a class method
def qux(x):
    print 'executing qux(%s)' % (x,)

class A(object):
    pass

a =
