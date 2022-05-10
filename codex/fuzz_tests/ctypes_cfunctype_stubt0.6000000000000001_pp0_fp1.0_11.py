import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    return "A string"

print(fun())
</code>
output:
<code>b'A string'
</code>
How can I make <code>fun()</code> return a normal string?
I tried:
<code>print(str(fun()))
</code>
But I get an error:
<code>TypeError: decoding to str: need a bytes-like object, LP_c_char_p found
</code>

edit:
I am using Python 3.6.5 on Windows 7.


A:

You need to specify the ctypes return type as <code>ctypes.c_char_p</code> to get the correct type
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
&gt;&gt;&gt; @FUNTYPE
... def fun(): 
...     return "A string"
...
&gt;&gt;&gt; print(fun())
b'A string
