fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should print a traceback with an exception.
"""
Traceback (most recent call last):
  File "../python/pyobject.c", line 654, in PyObject_Call
  File "../python/pyobject.c", line 839, in PyEval_CallObjectWithKeywords
  File "./test/test_pyobject.py", line 11, in <module>
    fn()
  File "./test/test_pyobject.py", line 10, in fn
    fn.__code__ = gi
TypeError: 'generator' object is not assignable
"""
