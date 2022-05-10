import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return lambda x: x
fun()
</code>
Here's what happens by default, when <code>sys.getrecursionlimit()</code> is 1000. 

Starting with the frame at the top of the stack, the code checks whether the frame has a <code>__code__</code> attribute. (This happens in <code>frame_gettracefunc</code>.) 
It looks like CPython "knows" that this function has a <code>__code__</code> attribute, so it doesn't check that attribute. Instead, it reads the <code>co_flags</code> field from that code object. 
It's not clear from the source whether it knows that it's a built-in function, but it checks that the <code>CO_GENERATOR</code> flag isn't set. (Because the generator flag is set on some but not all user-defined generator functions, checking for generators is a proxy for checking for user-defined functions.)
It then uses the <code>__wrapped__</code> attribute from the code object (which is a <code>PyWrapperDescrObject</code>) to get at
