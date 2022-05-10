import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = 1
    m.close()
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0] = 1
TypeError: 'mmap.mmap' object does not support item assignment
</code>
The documentation says:
<blockquote>
<p>The mmap() function returns a memory-mapped file object. The mmap
  constructor takes flags, prot, and access arguments. The flags and
  prot arguments are the same as the flags and prot arguments to the
  mmap() system call, but the access argument is <strong>new</strong> and must be one of
  ACCESS_READ, ACCESS_WRITE, or ACCESS_COPY.</p>
</blockquote>
What's the deal?


A:

You have opened the file for reading and writing with <code>'r+b'</code>. That's why you have to use <code>ACCESS_WRITE</code> for the <code>access
