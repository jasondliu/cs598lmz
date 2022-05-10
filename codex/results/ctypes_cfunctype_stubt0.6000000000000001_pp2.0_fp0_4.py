import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

def g():
    for i in range(10):
        f()

g()
</code>
When compiled with <code>pypy-c</code> and run, this prints:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
  File "test.py", line 8, in g
  File "test.py", line 7, in f
  File "test.py", line 3, in fun
Fatal RPython error: Exception: &lt;Exception: NoneType not callable&gt;
</code>
It seems to be a bug in the JIT, which does not handle <code>None</code> as a return value well.

