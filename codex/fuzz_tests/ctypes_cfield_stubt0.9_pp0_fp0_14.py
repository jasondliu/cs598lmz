import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Or, C wouldn't define global class variables. Or, they would translate these to static variables, not globals. In either case, these requirements could be met but would break the standards-conformance guarantee.
As it is, getattr has the desired behaviour. The hack you propose seems to work, at first. But it stops working with more complex usage. For example:
<code>def f(s):
    for i in range(10):
        print(s)

f('a')
print(f.func_defaults)
</code>
When tracing this code, Python will try to look up the <code>func_defaults</code> attribute in the globals. As we've just seen, it doesn't find it there, so it looks it up in the builtins. So now you have to override the getattribute method in the builtins as well. And then you have to propagate this attribute via <code>__dict__.__getattribute__</code>. You could make this work, with enough effort. But it will be fragile and ugly.

