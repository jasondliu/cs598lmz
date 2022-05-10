import ctypes
ctypes.cast(id(m), ctypes.py_object).value

output:
&lt;module 'math' (built-in)&gt;
</code>
I can't figure out how to import it, so that I can call it by name.
<code>import ctypes
m = ctypes.cast(id(m), ctypes.py_object).value

output:
NameError: name 'm' is not defined
</code>
I realize that it's not really necessary to import it, but still wonder why I'm unable to.


A:

<code>m = ctypes.cast(id(m), ctypes.py_object).value
</code>
That's trying to use the name <code>m</code> before the line defines <code>m</code>.
More generally, the <code>id</code> is not defined by Python; the CPython implementation uses the address of the object as the ID, but that's an implementation detail. It's not guaranteed to be unique for all objects, or even for all objects of the same type.

