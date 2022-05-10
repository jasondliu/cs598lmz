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
print repr(latefin.ref())
</code>
The error occurs in branch <code>if (numfree != 0)</code> before <code>failed = 1;</code>, where it does <code>goto fast_block;</code>, thus falling through to the end and decrementing <code>tp-&gt;ob_refcnt</code>. If you run this program under a debugger and pause in <code>decref_slow</code> (which I used gbd rather than pdb to do), you'll see that the reference count is -1, though it's only -1 after the <code>--</code>, not before.
I went on to check out <code>__dealloc</code> as well as modify this example. In the latter case, if <code>numfree == 0</code>, the <code>tp-&gt;ob_refcnt</code> eventually reaches <code>-sys.getrefcount(obj)</code> (also the object memory is initialized with <code>memset(p, 'd', size);</code>, even when the object memory actually
