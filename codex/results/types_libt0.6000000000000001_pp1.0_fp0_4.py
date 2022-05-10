import types
types.MethodType(foo, 2)
</code>
TypeError: descriptor 'foo' of 'int' object needs an argument
However, I can do this:
<code>class A:
    pass

def foo(self):
    return 1

a = A()
a.foo = types.MethodType(foo, a)

a.foo()
</code>
1
I've read up on descriptors, but it doesn't seem to make sense to me. Can anyone explain what's going on here?


A:

<code>int</code> objects are immutable, and the <code>__init__</code> descriptor is used to make a new instance. <code>a = A()</code> creates a new instance of <code>A</code> and calls <code>A.__init__(a)</code> to initialize it.
<code>int</code> objects are immutable, so you can't create a new instance of <code>int</code> and initialize it.

