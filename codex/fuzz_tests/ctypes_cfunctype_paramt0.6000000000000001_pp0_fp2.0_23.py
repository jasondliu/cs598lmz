import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Foo:
    def __init__(self):
        self.x = 42

    def callback(self, y):
        print self.x, y
        return y

f = Foo()

f.callback(5)

cfunc = FUNTYPE(f.callback)
</code>
However, when I try to run this I get a <code>TypeError: &lt;unbound method Foo.callback&gt; is not a Python function</code> error. I know that I can use <code>ctypes.pythonapi.PyCObject_AsVoidPtr</code> to get the address of the object, but I don't know how to use that to create a callable object. 


A:

I realized that the right way to do this is to actually use the <code>pythonapi</code> module:
<code>import ctypes

class Foo:
    def __init__(self):
        self.x = 42

    def callback(self, y):
        print self.x, y
        return
