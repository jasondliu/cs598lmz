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
gc.collect()

print(latefin.ref() is None)
</code>
This should not print <code>True</code>, but on my system it does. 
How can I prevent this from happening?
EDIT: I've tried this on two different versions of CPython: 3.4.3 and 3.4.4. Both exhibit the same behavior.


A:

You are creating a cyclic reference in a <code>__del__</code> method, and the garbage collector is not able to free this object, thus the <code>__del__</code> method is never called. From the documentation:
<blockquote>
<p>Note that when a finalizer is invoked, it is invoked not in the
  context of the object being finalized (which no longer exists at that
  point), but in the context of the object’s type.</p>
</blockquote>
And:
<blockquote>
<p>Finalizers execute during the collection of the garbage collector.
  This means that they cannot reference the object being finalized anymore. Additionally, the garbage collector has the option
