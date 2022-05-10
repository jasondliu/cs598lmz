import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'hello world'

def show(s):
    print(s, type(s))

for fun in (show, show):
    print(fun(fun()))
</code>
output:
<code>b'hello world' &lt;class 'bytes'&gt;
b'hello world' &lt;class 'bytes'&gt;
</code>

