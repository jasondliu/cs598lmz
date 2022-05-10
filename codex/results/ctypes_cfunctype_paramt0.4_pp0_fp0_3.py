import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print x
    return x

cb = FUNTYPE(callback)

dll = ctypes.CDLL('test.dll')
dll.callback(1, cb)
</code>
The dll is compiled from the following C code:
<code>#include &lt;stdio.h&gt;

typedef int (*callback_t)(int);

int callback(int x, callback_t cb) {
    int y = cb(x);
    printf("%d\n", y);
    return y;
}
</code>
The problem is that the callback is called twice. The first time the callback is called, it is called with the correct value, but the second time it is called with an incorrect value.
The output looks like this:
<code>1
1
0
</code>
The callback is called twice because <code>printf</code> is called twice. The first time <code>printf</code> is called, the correct value is printed, but the second time,
