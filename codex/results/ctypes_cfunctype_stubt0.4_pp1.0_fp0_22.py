import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
print(type(fun))
print(fun.__name__)
print(fun.__doc__)
print(fun.__module__)
print(fun.__dict__)
print(fun.__defaults__)
print(fun.__closure__)
print(fun.__code__)
print(fun.__globals__)
print(fun.__annotations__)
print(fun.__kwdefaults__)
print(fun.__self__)
</code>
Output:
<code>42
&lt;class 'function'&gt;
fun
None
__main__
{}
None
None
&lt;code object fun at 0x7f7f6d2c1a80, file "fun.py", line 4&gt;
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': &lt;_frozen_importlib_external.SourceFileLoader object at 0x7f7f6d2c1f98&gt;
