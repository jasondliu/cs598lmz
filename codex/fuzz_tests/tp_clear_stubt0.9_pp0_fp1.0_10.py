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
del func, cyc, LateFin, Cyclic
gc.collect()

del latefin
gc.collect()

print(func)
"""

del LateFin
gc.collect()

def func():
    return 2

latefin = LateFin()
cyc = tuple.__new__(Cyclic, (func, latefin))
func.__module__ = cyc
del func, cyc, LateFin, Cyclic
gc.collect()

del latefin
gc.collect()
print(func)
""".format(sys.executable, subprocess.list2cmdline(additional_args))

    def test_19468(self):
        import subprocess
        proc = subprocess.Popen([sys.executable, "-c",
                                 "import os, sys; sys.stdout.write(os.getcwd())"],
                                cwd=bytes(os.path.dirname(__file__), "ascii"),
                                universal_newlines=True,
                                stdout=subprocess.PIPE)
        cwd = proc.communicate()
