import types
types.MethodType(func, obj)
</code>
<code>types.MethodType</code> is a class which implements a method for a particular object, and is generally not used directly. 
However, you can use <code>types.MethodType</code> to add a method to a class after the class has already been defined, as in the following example:
<code>import types

def my_method(self, x):
    return x

class Foo(object):
    pass

Foo.my_method = types.MethodType(my_method, Foo)

a = Foo()
print a.my_method(5)
</code>
output:
<code>5
</code>

