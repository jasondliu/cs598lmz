import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_byte, ctypes.c_int, ctypes.c_int)

def c_callback(parm1, parm2):
    print(parm1,parm2)
    return 1

callback = FUNTYPE(c_callback)
</code>
I get:
<code>{&lt;class 'ctypes.CFUNCTYPE'&gt;: [convert_py2c_callback, &lt;class 'ctypes.CFUNCTYPE'&gt;]}
Traceback (most recent call last):
  File "C:\Python33\lib\site-packages\ctypes\__init__.py", line 353, in _check_callbacks
    raise TypeError(msg) from None
TypeError: must be convertible to a pointer, not CFUNCTYPE
</code>
So:

What is the proper type for ctypes.c_void_p ?
Where can I find a list of the types that are acceptable for ctypes.c_void_p.
What is the proper way to convert the ctypes.CFUNCTY
