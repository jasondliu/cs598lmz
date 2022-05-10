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

if __name__ == "__main__":
    import sys
    if sys.platform == "win32":
        from test import test_support
        test_support.subprocess_helper(__file__, True)
</code>
Here is the output of running the script:
<code>&gt; python test_cycle.py
[100, 100]
[100, 100]

&gt; python2.6 test_cycle.py
[100, 100]
[100, 100]

&gt; python3.3 test_cycle.py
[100, 100]
[100, 100]

&gt; python2.6 test_cycle.py --subprocess
[100, 100]
[100, 100]

&gt; python3.3 test_cycle.py --subprocess
[100, 100]
[100, 100]

&gt; python3.4 test_cycle.py
[100, 100]
[100, 100]

&gt; python3.4 test_cycle.py --
