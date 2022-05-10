import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
You can get a reverse mapping of type to name using a dictionary comprehension and the above mapping, like so:
<code>&gt;&gt;&gt; type_name_map = {v.__name__: k for k, v in name_type_map.items()}
&gt;&gt;&gt; type_name_map
{'c_int': 'x', 'c_byte': 'b', 'c_uint': 'i', 'c_ulonglong': 'L', 'c_double': 'd', 'c_float': 'f', 'c_short': 'h', 'c_longlong': 'q', 'c_long': 'l'}
&gt;&gt;&gt; type_name_map['c_int']
'x'
</code>
If you want a single unified mapping, use <code>ChainMap</code> from the <code>collections</code> module, like so:
<code>&gt;&gt;&gt; from collections import ChainMap
&gt;&gt;&gt; name_type_map
