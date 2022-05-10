import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)
fun()

# without ctypes
def fun():
    return (1,2,3)
fun()
</code>
This is a simplified example of course, but the point is that I want to use the same code for both cases. I've tried to use <code>if</code> statements like this:
<code>if isinstance(ctypes.py_object):
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def fun():
        return (1,2,3)
    fun()

if not isinstance(ctypes.py_object):
    def fun():
        return (1,2,3)
    fun()
</code>
but that doesn't work. I think it's because I'm using <code>isinstance</code> wrong, but I'm not sure. Any ideas?


A:

<code>isinstance</code> is used with two arguments, and you're only supplying it with one. 
<code>if isinstance(ctypes.py_object
