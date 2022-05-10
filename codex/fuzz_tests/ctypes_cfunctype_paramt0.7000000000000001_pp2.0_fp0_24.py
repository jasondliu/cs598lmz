import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_double)
def callback(val):
    print("callback")
    print(val)
callback_func = FUNTYPE(callback)

x = ctypes.c_double(0.0)
x_ptr = ctypes.pointer(x)

lib_dll.call_func(callback_func, x_ptr)
#lib_dll.call_add(ctypes.c_double(2.0), ctypes.c_double(3.0))
</code>
This is the output I get from the above code:
<code>&gt;&gt;&gt; 0.0
</code>
I can't for the life of me figure out what's going on.
I'm using Python 3.6.1 on Windows 10.
Any help would be appreciated.
UPDATE
If I change the <code>call_func</code> function in the C code to this:
<code>double call_func(void (*cb)(double)) {
    double val = 2.0;
    cb(val);
    return val;
