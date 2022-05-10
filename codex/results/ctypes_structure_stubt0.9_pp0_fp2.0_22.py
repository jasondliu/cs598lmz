import ctypes

class S(ctypes.Structure):
    x = bytearray(100)

s = S()
print(ctypes.sizeof(type(s.x)))
print(ctypes.sizeof(s))
</code>
see also:
<code>$ python3
Python 3.6.0 (default, Jan 13 2017, 00:00:00) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; class S(ctypes.Structure):
...   x = bytearray(100)
... 
&gt;&gt;&gt; s = S()
&gt;&gt;&gt; type(s.x)
&lt;class 'bytearray'&gt;
&gt;&gt;&gt; s.x = b'asdjkfhasdlkfhaslkd'
&gt;
