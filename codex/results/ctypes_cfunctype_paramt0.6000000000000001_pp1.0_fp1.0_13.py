import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Test(object):
    def __init__(self):
        self.fun = FUNTYPE(self.test)

    def test(self, a):
        return a


def test(a):
    return a

t = Test()
print t.fun(10)

fun = FUNTYPE(test)
print fun(10)
</code>
The output is:
<code>10
&lt;__main__.FUNTYPE object at 0x7f1c1d9c9d10&gt;
</code>
Why does the <code>FUNTYPE</code> object not call <code>test</code>?


A:

The <code>__init__</code> method of the <code>Test</code> class is not called.
<code>&gt;&gt;&gt; t = Test()
&gt;&gt;&gt; t.fun(10)
&lt;__main__.FUNTYPE object at 0x7f2c6d5b6d10&
