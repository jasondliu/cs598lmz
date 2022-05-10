import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.close()
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
What am I doing wrong?


A:

<code>mmap</code> needs the size of the file to map it. You can use <code>os.path.getsize</code> for that:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), os.path.getsize('test'))
    m.write(bytes(1))
    m.close()
</code>

