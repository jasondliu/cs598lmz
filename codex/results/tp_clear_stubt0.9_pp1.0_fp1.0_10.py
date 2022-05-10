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
del func, cyc, LateFin, Cyclic, weakref
gc.collect()
del latefin, latefin
gc.collect()
</code>
Execution of this code results in a <code>Segfault</code> during the call to <code>collect()</code> on the last line. My question is - is this behavior mandated by the language or is it an implementation bug?
Note:
<code>$ python
Python 2.7.13 (default, Mar  6 2017, 12:09:41) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; from sys import version_info as v
&gt;&gt;&gt; print(v.major, v.minor, v.micro)
2 7 13

gcc --version
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr
