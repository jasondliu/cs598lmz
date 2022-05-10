import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1


dll = cdll.LoadLibrary('..\..\bin\Release\TraceVPython.dll')
dll.init_graphics(fun())
dll.set_background(fun(),.3,.3,.3)
dll.draw_graph(fun(),-2,-2,2,2)
dll.interact()

print 'This will never be printed'
</code>
As you can see, I am using <code>__pycache__</code> directories and I have also tried using the <code>sys.setrecursionlimit()</code> function to increase the limit. I do not think it is a problem with the build, since it worked for me on my pc but that maybe a wrong assumption.
I have also tried searching for this error but all results point to problems with python rather than the actual code, and those solutions have not worked for me.
Any insight into why this is happening would be greatly appreciated, and if more information is needed just ask and I will provide it.


A:

From the documentation:
<blockquote>
<p>Recursive calls to a Python function are allowed, as long
