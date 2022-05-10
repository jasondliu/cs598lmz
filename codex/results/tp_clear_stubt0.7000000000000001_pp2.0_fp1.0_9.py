import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()
func()
</code>
This causes a segmentation fault with python 2.7.3.  I think it should cause a <code>TypeError</code> exception, but I don't see any reason it should cause a segfault.  I'm running on OSX 10.8.2, but it happens on linux too.


A:

The <code>TypeError</code> message is:
<blockquote>
<p>'NoneType' object is not callable</p>
</blockquote>
So, you're trying to call a <code>None</code> object.
This is because you set <code>func</code> to <code>None</code>, then call it. And then, you set <code>func</code> to a <code>None</code> object, then call it.
I.e.:
<code>func = None
func()  # TypeError: 'NoneType' object is not callable

func = lambda: None
func()  # No error
</code>
I.e.:
<code>from types import Function
