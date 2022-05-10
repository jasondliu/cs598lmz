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
del LateFin, Cyclic
gc.collect()

print(latefin.ref)
</code>
This crashes with the following traceback (Python 3.6.1):
<code>Traceback (most recent call last):
  File "main.py", line 22, in &lt;module&gt;
    print(latefin.ref)
AttributeError: 'LateFin' object has no attribute 'ref'
</code>
Is this a bug?
Note that this issue is not specific to <code>tuple</code>, replacing <code>tuple</code> with <code>list</code> or <code>dict</code> in the code also causes a crash.
Edit:
This issue was reported to the Python bug tracker and has been marked as a duplicate of another bug that was fixed in Python 3.7.


A:

Yes, it's a bug.
The core of the issue is that the new <code>tuple</code> (later the <code>Cyclic</code> tuple) is being garbage-collected before <code>latefin</code> is garbage-collected
