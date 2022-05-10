import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

t = threading.Thread(target=fun,args=(),daemon=True)
t.start()
t.join()

print ("Done")
</code>
In a regular Python3 interpreter I get:
<code>$ env/bin/python3 t.py
Done
</code>
In pypy2 I get:
<code>$ env -p pypy2/bin/pypy /path/to/t.py
Done
</code>
In pypy3 I get:
<code>$ env -p pypy/bin/pypy /path/to/t.py
$ 
</code>
Note that at no point is the fun() function called, it just freezes at the call to t.start().
It also freezes if I remove the decorator (which I figured was an artifact at some point) or if I remove the daemon=True option.
Is it a bug? Shall I open an issue to their bug tracker or do I miss something?


A:

is it possible that it is stuck always trying to acquire thread lock (to create a thread
