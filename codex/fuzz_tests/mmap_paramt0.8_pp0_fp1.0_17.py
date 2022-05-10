import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(4)
</code>
In this code I am trying to change byte <code>1</code> to byte <code>4</code> using <code>mmap</code>.
However I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    m[0] = bytes(4)
TypeError: 'mmap.mmap' does not support the buffer interface
</code>
How can I change individual bytes in a file using <code>mmap</code>?


A:

You can't assign values to slices of a <code>mmap.mmap</code> object directly; you have to call <code>mmap.write</code> instead.
<code>m[0:1] = b'\x04'
</code>
It's easier and more idiomatic to work with the <code>memoryview</code> object returned by <code>mmap.memoryview()</code>, which
