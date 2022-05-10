from _struct import Struct
s = Struct.__new__(Struct)
s.size = 8

def pack(self, vals): 
    return b''.join(self.pack(*t) for t in vals) 

s.pack = pack

QQQQ = s.pack(itertools.repeat((1,), 4))

def QQQQ(i): 
    return b'\x01' * 4
</code>
so,
<code>pygtrie&gt; %timeit QQQQ(2)
10000000 loops, best of 3: 104 ns per loop
</code>

<code>itertools</code> can also be replaced with <code>operator</code> and <code>functools</code> and <code>collections</code> can also be replaced with <code>abc</code> and <code>types</code> but that's not really a win

<code>inspect</code> is used for building the documentation for _frozen_dict.py, _frozen_multidict.py, and _multidict_py.py.
<code>import sys, re,
