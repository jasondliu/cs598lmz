import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(0)
    m.close()
</code>
The <code>Traceback (most recent call last):</code> output:
<code>Traceback (most recent call last):
  File "mmaptest.py", line 10, in &lt;module&gt;
    m[0:1] = bytes(0)
ValueError: memoryview assignment: lvalue is not contiguous
</code>
Strange. Shouldn't the <code>bytes(0)</code> create a contiguous byte string with no issues? Changing the byte size to something other than 1 works fine, I confirmed that with extensive tests.


A:

<code>bytes(1)</code> yields a byte string with one character in it, which is not contiguous. Content-wise, it is equivalent to <code>bytes(' ', 'ascii')</code>.
To get an empty byte, use <code>bytes(0)</code> instead, or <code>b''</code>:
<code>m[0:1] = bytes(0)
</code>
or:
<
