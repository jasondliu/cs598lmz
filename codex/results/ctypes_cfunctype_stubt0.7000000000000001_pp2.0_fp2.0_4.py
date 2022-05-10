import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 42
print(fun())
</code>
I've linked a couple of related questions below, but I'm not sure if the answers apply to my case.
Is there a way to create a function pointer to a Python function?
How can I implement a callback function that has a void* argument in Python?


A:

Python functions are objects and they can be passed as arguments to other functions:
<code>&gt;&gt;&gt; def f():
...     return 42
...
&gt;&gt;&gt; def g(fun):
...     return fun()
...
&gt;&gt;&gt; g(f)
42
</code>
There's no need to use ctypes here.

