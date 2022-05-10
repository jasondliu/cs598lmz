import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but if I try to return a list, I get a segfault.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print fun()
</code>
I can't figure out what is wrong with this.  I've tried returning a tuple, and that works fine.  I've tried returning a list of strings, and that works fine.  I've tried returning a list of ints, and that segfaults.  I've tried returning a list of ints with a tuple in it, and that segfaults.  I've tried returning a list of ints with a tuple of ints in it, and that segfaults.  I've tried returning a list of ints with a tuple of strings in it, and that segfaults.  I've tried returning a list of ints with a tuple of strings in it and a tuple of ints in it, and that segfaults.
