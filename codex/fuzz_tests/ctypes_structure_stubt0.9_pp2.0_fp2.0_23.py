import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()

print S.x
</code>
Here's the output I get:
<code>$ python foo.py
&lt;Field type=c_longdouble, ofs=0:0, size=8:8&gt;
</code>
And, for comparison, a simple struct:
<code>$ python
&gt;&gt;&gt; import struct
&gt;&gt;&gt; struct.pack('&lt;d', 0.625)
'\x00\x00\x00\x00\x00\x00\x00\x03'
</code>
What I think is happening is that <code>ctypes</code> can't figure out which binary representation it should use, and assumes something that's incompatible with how I store my data. Its guessing is probably based on the platform I'm on currently, but like I said in the start, I'd like to avoid such a platform dependant approach.  
Does anyone know how to actually get <code>ctypes</code> to use little endian signed 64-bit IEEE 754 floating point numbers? 


