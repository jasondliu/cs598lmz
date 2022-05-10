import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
This is the code that I am using to get the address of the object.
<code>import ctypes

class Foo:
    pass

foo = Foo()
print("Address of foo:", ctypes.cast(id(foo), ctypes.py_object).value)
</code>
The output of the code is:
<code>Address of foo: &lt;__main__.Foo object at 0x7f11f6da3e10&gt;
</code>
How can I get the actual address of the object?


A:

You can use <code>ctypes.addressof</code> to get the actual address of the object:
<code>import ctypes

class Foo:
    pass

foo = Foo()
print("Address of foo:", ctypes.addressof(foo))
</code>

