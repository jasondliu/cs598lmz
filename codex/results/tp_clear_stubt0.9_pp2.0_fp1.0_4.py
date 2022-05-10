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
del latefin
</code>


A:

Yes, it would be uncommon, but not impossible.
One way this could happen is if instead of a function, <code>func</code> was an instance of a class with <code>__del__</code> implemented.  The way that classes have been defined in PyPy makes it so that a class will be garbage collected (and thus <code>__del__</code>ed) when the module containing its definition is deallocated.
Here is an example:
<code>class Foo:
    def __del__(self):
        print 'deleted'
import sys
foo = Foo()
del sys.modules[__name__] # delete the entire module
print 'done'
</code>
running this gives:
<code>deleted
done
</code>
In PyPy, there is no built-in function <code>delete</code>, but this example shows that the module cleanup is called at the same point as <code>__del__</code>.  Furthermore, what you are asking about is at least possible since <code>del sys.
