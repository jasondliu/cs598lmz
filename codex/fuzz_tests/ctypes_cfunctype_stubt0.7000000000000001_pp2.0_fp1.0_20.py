import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hey!"
</code>
I just get this error:
<code>&gt;&gt;&gt; fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Python32\lib\ctypes\__init__.py", line 357, in __call__
    return self.call(*args)
  File "C:\Python32\lib\ctypes\__init__.py", line 344, in call
    return self.func(*args)
  File "&lt;stdin&gt;", line 2, in &lt;lambda&gt;
  File "&lt;stdin&gt;", line 4, in fun
TypeError: 'str' object is not callable
</code>
I would really appreciate any help on this!


A:

<code>&gt;&gt;&gt; fun = ctypes.CFUNCTYPE(ctypes.py_object)(lambda: "hey!")
&gt;&gt;&gt;
