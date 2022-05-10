import ctypes
ctypes.cast(object, ctypes.py_object)

def bad_one(a):
    return a + 1

def bad_two():
    return ctypes.cast(bad_one, ctypes.py_object)
</code>
will throw with <code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1</code>.
This is because <code>bad_one</code> is not a ctypes <code>CFUNCTYPE</code> type. If <code>bad_one</code> is defined thus:
<code>@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
def bad_one(a):
    return a + 1
</code>
then <code>bad_two</code> will work as expected.

