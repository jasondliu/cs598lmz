import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    try:
        return [1]
    except ValueError:
        return 'error'

class A(object):
    def __init__(self, func):
        self.func = func
    def __del__(self):
        self.func()

a = A(fun) # segmentation fault

print("ARRIVED HERE")
</code>


A:

<code>fun</code> is a Python function, not a closure, because closures are only created if the function is declared inside another function, and uses variables from the surrounding code. The bug is that CPython doesn't support Python functions as callbacks.
To build a closure, use the lambda statement:
<code>&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
&gt;&gt;&gt; fun = FUNTYPE(lambda: 'error' if True else [1])
&gt;&gt;&gt; class A(object):
...     def __init__(self, func):
...         self.func = func
...     def __del
