import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def make_callback(func):
    return FUNTYPE(func)

def callback(x):
    print "In python callback", x
    return x

cb = make_callback(callback)

lib.call_back(cb)
</code>
The C code:
<code>#include &lt;stdio.h&gt;

int call_back(int (*cb)(int))
{
    int x = cb(1);
    printf("In C callback %d\n", x);
    return x;
}
</code>
The output:
<code>In python callback 1
In C callback 1
</code>

