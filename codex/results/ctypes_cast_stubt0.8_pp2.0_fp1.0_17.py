import ctypes
ctypes.cast(1337, ctypes.py_object)
</code>
when doing this from ctypes,
<code>&gt;&gt;&gt; ctypes.pythonapi.PyLong_AsVoidPtr.restype = ctypes.c_void_p
&gt;&gt;&gt; ctypes.pythonapi.PyLong_AsVoidPtr(ctypes.py_object(1337))
1337
</code>
although the docs there are slightly misleading. They make it sound like PyLong_AsVoidPtr is deprecated, but they're actually talking about the PyLong->void* conversion. So you'd probably want to use <code>PyLong_AsUnsignedLong</code> instead of <code>PyLong_AsVoidPtr</code> to get a consistent result.
FWIW, if you're looking for a "real" example, the python source for ctypes has a few. E.g. here:
<code>/usr/lib/python2.6/ctypes/macholib/mach_o.py:
    if r.type == LC_LOAD_DYLINK
