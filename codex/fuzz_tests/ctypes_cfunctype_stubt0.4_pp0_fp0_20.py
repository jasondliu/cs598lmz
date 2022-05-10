import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

@jit
def f():
    return fun()

print(f())
</code>
The result is the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    print(f())
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/numba/dispatcher.py", line 370, in _compile_for_args
    error_rewrite(e, 'typing')
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/numba/dispatcher.py", line 340, in error_rewrite
    reraise(type(e), e, None)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/numba/six.py", line 658, in reraise
    raise value
