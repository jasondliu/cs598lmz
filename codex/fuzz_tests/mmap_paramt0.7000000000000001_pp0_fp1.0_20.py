import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(0)
</code>
This works perfectly fine in Py2.
I get the following error in Py3:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0:1] = bytes(0)
TypeError: must be read-write buffer, not bytes
</code>
If I try to use bytearray instead of bytes, I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0:1] = bytearray(0)
TypeError: write() argument must be a bytes object
</code>
I really want to avoid using <code>m.seek()</code> and <code>m.write(b'\0')</code> if possible. It is much more elegant to be able to use <code>m[0:1]</code>.
How can I do this in python3?


A:

