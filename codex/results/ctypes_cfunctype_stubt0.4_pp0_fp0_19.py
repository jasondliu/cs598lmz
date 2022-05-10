import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
But it's not working for me. I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>
How can I get this to work?


A:

You need to call <code>ctypes.pythonapi.PyString_FromString</code> and return the result:
<code>from ctypes import pythonapi, c_char_p, py_object
FUNTYPE = ctypes.CFUNCTYPE(py_object)
@FUNTYPE
def fun():
    return pythonapi.PyString_FromString(c_char_p("hello"))

print fun()
</code>

