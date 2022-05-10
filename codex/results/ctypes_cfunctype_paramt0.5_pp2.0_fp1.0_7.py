import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def my_callback(x):
    print("Callback called with {}".format(x))
    return 0

CALLBACK = FUNTYPE(my_callback)

try:
    lib = ctypes.CDLL("./libcallback.so")
except OSError:
    print("Could not load library. Did you compile it?")
    sys.exit(1)

lib.register_callback(CALLBACK)
print("Registered callback")
lib.do_stuff()
print("Library finished doing stuff")
</code>
libcallback.c:
<code>#include &lt;stdio.h&gt;

int callback(int x);

void register_callback(int (*cb)(int))
{
    callback = cb;
}

void do_stuff()
{
    printf("Calling callback...\n");
    callback(42);
    printf("Callback returned.\n");
}
</code>
The output is as follows:
<code>$ python callback.py
Registered callback

