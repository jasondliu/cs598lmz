import types
types.MethodType(lambda self: self.foo(1), Foo())
</code>
This is the same as
<code>def bar(self):
    self.foo(1)

bar(Foo())
</code>
For the example you gave, it works because you're calling <code>Foo().foo</code> directly. This is equivalent to
<code>self = Foo()
self.foo(10)
</code>
This is equivalent to
<code>self = Foo()
def foo(self, x):
    print x * 100

foo(self, 10)
</code>

