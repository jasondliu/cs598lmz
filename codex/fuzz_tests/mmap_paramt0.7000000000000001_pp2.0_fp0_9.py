import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
</code>
but if I change the last line to <code>m[0] = b'0'</code> then I get a <code>mmap.error</code>
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    m[0] = b'0'
mmap.error: cannot modify size of memory mapping
</code>
Why is that?


A:

An object of type <code>bytes</code> is iterable, so when you <code>m[0] = b'0'</code>, Python expects you to provide a sequence of bytes to copy into <code>m</code> at index 0.  It iterates that object, copying in the bytes one at a time.
<code>mmap</code> is not designed to handle sequences of bytes, only single bytes.
If you want to assign a byte, then just assign the byte:
<code>m[0] = b'0'[0]
</code>

