import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    m.flush()  # fails here
</code>
I get the following error:
<code>File "mmap.py", line 8, in &lt;module&gt;
    m.flush()
AttributeError: 'mmap.mmap' object has no attribute 'flush'
</code>
I checked the documentation and they said:
<code>Python 3.3 added the flush() method.
</code>
So this is weird, because I use Python 3.6.
Is <code>flush</code> really not implemented in Python 3.6 or did I misunderstand something?


A:

You can use <code>mmap.mmap.close()</code>: 
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    m.close()
