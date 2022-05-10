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

gc.collect()   # get rid of the late-triggering __del__

from subprocess_helper import subprocess_main
subprocess_main(["-c", "from sys import stdin, stdout; gc.collect();path = stdin.read(); exec(compile(stdin.read(), path, 'exec'), {'__builtins__': None}, stdin.read()).dump(stdout)"])
</code>


A:

I have found a solution:

Give the path to the <code>run_python.c</code> file to the <code>subprocess_main</code> function
Store the source code in a file, and give the path to that file to the first <code>subprocess.Popen</code> (instead of piping the source code)

For example (this code is only a quick test, and doesn't use the <code>subprocess_main</code> function):
<code>import marshal, subprocess, shutil, pathlib


code = """
def f(code):
    module
