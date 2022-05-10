import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test(n):
    for i in range(n):
        fun()

test(1000000)
</code>
On my machine, this takes about 0.4 seconds.

