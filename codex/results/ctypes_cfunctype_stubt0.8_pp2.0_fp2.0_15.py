import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "fun()"
    return "OK"
handle = ctypes.windll.kernel32.GetModuleHandleA(None)
print handle
mydll = ctypes.WinDLL(handle)
mydll.fun = fun
print handle
ctypes.windll.kernel32.MessageBoxA(None, "hello","hello", 0)
</code>
How can I use <code>mydll</code> to call <code>fun()</code> like
<code>mydll.fun()
</code>
but not
<code>mydll.fun
</code>
and the result of it is "OK",not "fun()"
Can you help me? Thanks.


A:

You need to make a real function object.
You can create a function object like this:
<code>mydll.fun = lambda : fun()
</code>
The lambda will call fun(), which will call the actual function.  You can also assign fun.__call__ to mydll.fun and it'll work the same way.
You can also create a real function object like this:
<code>my
