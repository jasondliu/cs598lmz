import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del view
</code>
This works fine with CPython, but crashes with PyPy:
<code>Fatal Python error: deallocating None
</code>
PyPy 7.3.2-beta0+d8e8b57aa1 on Darwin, Python 3.7.2.


A:

PyPy's garbage collector is a replacement for the reference counting scheme CPython uses, but it does not collect objects as early as CPython does. In particular, it does not collect <code>BufferedReader</code> instances, which are used by <code>io.open</code> for reading, immediately after their reference count hits zero. Instead, it relies on the destructor to clear <code>f.raw</code> and the <code>weakref</code> in <code>f._weakref</code>. When the destructor runs, the object <code>f.raw</code> refers to has already been collected, so the destructor crashes.
This can be fixed with a simple patch to <code>io</code>.patch:
<code>diff --git a/pypy/module/sys/src/p
