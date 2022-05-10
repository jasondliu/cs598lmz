import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
I don't know how to interpret the error message:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "test.py", line 11, in &lt;module&gt;
    m[0] = b'2'
TypeError: must be read-write buffer, not memoryview
</code>
What is a memoryview and how do I create one? Is there some other way of creating an mmap object?


A:

I don't have an answer for why your code fails, but the following does work:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

