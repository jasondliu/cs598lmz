import types
types.MethodType(foo, 1)

# TypeError: descriptor 'foo' of 'int' object needs an argument
</code>
The error is clear enough. I am trying to use a method on an object that does not implement it.
But the thing is, I am not trying to call <code>foo</code> on <code>1</code> or any other <code>int</code>. I am trying to create a new method and assign it to <code>1</code>, which is perfectly valid:
<code>def foo(self):
    pass

def bar(self):
    pass

1.foo = types.MethodType(foo, 1)
1.bar = types.MethodType(bar, 1)
</code>
Why does <code>types.MethodType</code> care about the target object?

