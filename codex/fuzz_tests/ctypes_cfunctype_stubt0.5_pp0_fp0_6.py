import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class C(object):
    def __init__(self):
        self.f = fun

c = C()
c.f()

c.f = fun
c.f()
</code>
The output:
<code>1
1
</code>
I have no idea why it works.

