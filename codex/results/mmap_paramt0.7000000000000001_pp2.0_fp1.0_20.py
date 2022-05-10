import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'2'
</code>
This will crash with
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[:] = b'2'
TypeError: Type str doesn't support the buffer API
</code>
The crash is caused by the following line in <code>mmap</code>:
<code>if isinstance(value, str):
    value = value.encode('ascii')
</code>
<code>m[:] = b'2'</code> is syntactic sugar for <code>m.__setitem__(slice(None), b'2')</code>.
The value coming in is a <code>bytes</code> object. But <code>mmap.__setitem__</code> converts it to a <code>str</code> object by calling <code>object.__str__</code>.
The <code>bytes.__str__</code> method is implemented in C, and it's defined to return the "printable" representation of the string
