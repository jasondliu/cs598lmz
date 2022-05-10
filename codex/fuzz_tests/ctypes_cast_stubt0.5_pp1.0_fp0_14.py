import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# using _PyObject_GetDictPtr
import ctypes
ctypes.pythonapi._PyObject_GetDictPtr(ctypes.py_object(obj))
</code>
The first one works, but the second returns <code>None</code>.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; class Foo(object): pass
... 
&gt;&gt;&gt; foo = Foo()
&gt;&gt;&gt; foo.__dict__
{}
&gt;&gt;&gt; ctypes.cast(id(foo), ctypes.py_object).value
&lt;__main__.Foo object at 0x7f5e1c2c4d10&gt;
&gt;&gt;&gt; ctypes.pythonapi._PyObject_GetDictPtr(ctypes.py_object(foo))
&gt;&gt;&gt; 
</code>
What's the difference between the two?


A
