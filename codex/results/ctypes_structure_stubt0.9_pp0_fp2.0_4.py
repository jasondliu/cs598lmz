import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 5

with closing(asmmemview(S)) as view:
    view.x[3] = ctypes.c_int(3)

print S()
</code>
and I get 
<code>% python structure-view.py
Traceback (most recent call last):
  File "structure-view.py", line 8, in &lt;module&gt;
    view.x[3] = ctypes.c_int(3)
AttributeError: 'AsmMemoryView' object has no attribute 'x'
</code>
The error comes from <code>__setattr__</code> definition:
<code>def __setattr__(self, name, value):
    try:
        field = getattr(type(self), name)
    except AttributeError:
        raise AttributeError("{0} object has no attribute {1}".format(type(self).__name__, name))
</code>
I guess fields get their definition during the <code>__init__</code> pass, which happens after <code>with
