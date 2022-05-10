import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine and prints <code>hello</code> as expected.
However, if I try to return a <code>ctypes.c_char_p</code> instead:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get a <code>TypeError</code>:
<code>TypeError: must be string without null bytes or None, not str
</code>
I've tried <code>ctypes.c_char_p("hello")</code> and <code>ctypes.c_char_p(b"hello")</code> but neither works.
How can I return a <code>ctypes.c_char_p</code> from a <code>ctypes.CFUNCTYPE</code> decorated function?


A:

<code>ctypes.c_char_p</code> is a pointer to a C string,
