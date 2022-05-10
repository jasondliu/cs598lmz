import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
FUNTYPE = ctypes.CFUNCTYPE(None)

LIB = ctypes.CDLL('./libtest.so')
FUNTYPE = ctypes.CFUNCTYPE(None)
LIB.testfunc.restype = FUNTYPE

@LIB.testfunc
def mycallback():
    print('Callback from C!')

mycallback()
</code>
If there is no <code>@LIB.testfunc</code> decorator, this prints <code>&lt;__main__.CFUNCTYPE_0000000002A3E3B0 object at 0x7fda1eab7610&gt;</code>.
When I add it, I get a Crash Window:
<code>Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)
</code>
What am I doing wrong?


A:

The code crashes because you are not returning an <code>int</code> value in your callback function. This is because the function prototype you set for it is <code>ctypes.CFUNCTYPE(ctypes.
