import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from mmap - msync failed
</code>
Note, that in my original code, I was not trying to read from the mmap. I was trying to write to it.
Can someone explain why this is happening and how to avoid it?
Edit:
After reading the answer, I would like to mention a few things:

In the original code I was writing to the mmap, not reading. The read was just a test to see what happens.
I am using a 64-bit Ubuntu 12.10.
I have tried both Python 2.7.3 and 3.2.3 and got the same error.
The exception is thrown immediately after the call to truncate.
A similar error can be reproduced by calling <code>m.resize(0)</code> instead of <code>f.truncate()</code>.



A:

This is a bug in the Python implementation.

