import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u"\U0001f603"
&gt;&gt;&gt; fun()
u'\U0001f603'
</code>
And also tested with this one:
<code>&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_char_p)
&gt;&gt;&gt; @FUNTYPE
... def fun(a):
...     return a
&gt;&gt;&gt; fun(u"\U0001f603")
u'\U0001f603'
&gt;&gt;&gt; fun("a")
'a'
&gt;&gt;&gt; 
</code>
However, when called from a C function, it returns the following:
<code>&gt;&gt;&gt; fun.restype = ctypes.c_char_p
&gt;&gt;&gt; fun.argtypes = []
&gt;&gt;&gt; _ = ctypes.CDLL(ctypes.util.find_library('
