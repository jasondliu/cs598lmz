import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
However, I am getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: write() argument must be str, not bytes
</code>
I have tried replacing <code>m[0] = b'\x00'</code> with <code>m[0] = '\x00'</code> and <code>m[0] = '0'</code> but I get the same error. I am using Python 2.7.


A:

<code>mmap</code> objects in Python 2 are byte strings, and you can only assign byte strings to them.
You could use <code>m[0:1] = b'\x00'</code> instead; that replaces the first byte with the byte you want to use instead.

