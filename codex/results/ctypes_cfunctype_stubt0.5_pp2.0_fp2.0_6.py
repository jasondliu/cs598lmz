import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
But this is not very convenient, because the only way to create the function type is to use the <code>CFUNCTYPE</code> constructor. This means that your code has to be aware of the fact that you're using the <code>ctypes</code> module.
It would be much more convenient if you could just create a function type in Python, with a syntax like <code>function(int, int) -&gt; int</code>. This would be much easier to use, and would make it easier to write code that is agnostic about the underlying implementation.
So, my question is, is there any way to create a function type in Python?

