import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a,b,c,d,e):
    print(a,b,c,d,e)

lib.myfunc = FUNTYPE(myfunc)
</code>
When I call <code>lib.myfunc(1,2,3,4,5)</code> I get the error <code>OSError: exception: access violation writing 0x00000000</code>. What am I doing wrong here?


A:

Your function signature is incorrect for the function you are calling.  The signature of <code>myfunc()</code> in C is:
<code>void myfunc(int a, int *b, int *c, int *d, int *e)
</code>
The function takes a single <code>int</code> and four pointers.  You are calling it with a single <code>int</code> and four values.
In order to use your function, you need to do something like this:

