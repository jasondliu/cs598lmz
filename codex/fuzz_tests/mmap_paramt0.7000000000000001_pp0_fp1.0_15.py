import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
I have no idea what is going on but I keep on getting this error:
<code>TypeError: an integer is required
</code>
I have tried using bytearray and 
<code>bytes(1, 'utf-8') 
</code>
instead of 
<code>bytes(1) 
</code>
but to no avail.


A:

You can't use <code>bytes(1)</code> to create a bytestring of length 1. This creates a bytes object of length 1 initialized with the value 1:
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
</code>
You can use a one-item tuple to create a bytestring of length one:
<code>&gt;&gt;&gt; bytes((1,))
b'\x01'
&gt;&gt;&gt; bytes((2,))
b'\x02'
</code>
The reason for this is that <code>bytes(1)</
