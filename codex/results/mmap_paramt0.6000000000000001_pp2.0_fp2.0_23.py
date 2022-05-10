import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
    m.flush()
    m.close()
</code>
And this is the exception I get:
<code>Traceback (most recent call last):
  File "so.py", line 8, in &lt;module&gt;
    m[0] = 1
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Why is it happening?


A:

The <code>mmap</code> object is not designed to work with <code>bytes</code> or <code>bytearray</code> objects. Use a <code>memoryview</code> instead:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = memoryview(bytes(1))[0]
    m.flush()
    m.close()
</code>
Demo:
<code>&gt
