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
</code>
Note I had to make <code>func.__module__</code> refer to <code>cyc</code> in order to trick <code>inspect</code> into creating a <code>LateFin</code>. I had to name the lambda and make it global in order to trick python into keeping an internal reference to it.
If I didn't do that, you'd have to add:
<code>import weakrefkey
latefin.ref = weakrefkey.weakrefkey(func)
</code>
to keep a reference to it.
It will still show that the objects are alive, but that's because we've tricked <code>inspect</code> into creating a reference.
As for fixing it, I'm not sure that's possible. I fear that you need the entire object hierarchy to be rooted in order for <code>gc.get_referrers</code> to work.

