import ctypes
ctypes.cast(id(obj), ctypes.py_object).value
&gt;&gt;&gt; obj
</code>
Is there a better or safer way to get the reference to the object without the id() call?


A:

Unfortunately, <code>id()</code> is the standard way to get the object's identifier. It will always have the same value for a given object, and it can't be changed by user code, so it's reliable (though not ideal).

