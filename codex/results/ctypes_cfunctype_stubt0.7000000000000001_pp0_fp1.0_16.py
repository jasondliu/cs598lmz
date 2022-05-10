import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

print fun()
</code>
Demo:
<code>$ python -m ctypes.util --find-library libpython2.7
libpython2.7.dylib
$ python -m ctypes.util --find-library libpython2.7 --strip-dirs
/usr/lib/libpython2.7.dylib
$ python2.7 test.py
hello world
</code>

