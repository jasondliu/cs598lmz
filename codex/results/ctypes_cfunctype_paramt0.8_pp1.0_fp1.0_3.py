import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double)

def f():
    print "ok"

c_f = FUNTYPE(f)

for i in range(1):
    c_f(1.234)
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    c_f(1.234)
  File "C:\Python27\lib\ctypes\__init__.py", line 364, in __call__
    self._a
