import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    return a + b

cb = FUNTYPE(callback)

lib = ctypes.CDLL("./libtest.so")
lib.test(cb)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    lib.test(cb)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 378, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 383, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
The C function is defined as follows:
<code>int
