import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
</code>
The problem is, when I run the program I get the following error:
<code>TypeError: expected LP_CFUNCTYPE, got &lt;class 'function'&gt;
</code>
I don't understand this error, because I have explicitly told the interpreter that I want a function, by using <code>@FUNTYPE</code>.


A:

You seem to be confusing the <code>ctypes.CFUNCTYPE</code> type with the <code>ctypes.CFUNCTYPE</code> factory. The type is <code>ctypes.CFUNCTYPE</code>, the factory is <code>ctypes.CFUNCTYPE()</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
</code>
In this code, <code>FUNTYPE</code> is the type, and <code>FUNTYPE()</code> is the factory.
The <code>__init__</code>
