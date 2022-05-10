import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot resize memory map
</code>
I'm using Python 3.4 on Mac OS X 10.10.3.
I tried adding <code>m.resize(0)</code> after the truncate, but it didn't help.
Why does this happen and how can I fix it?


A:

The <code>mmap</code> module is not designed to work with files that are being truncated.  The <code>mmap</code> module is designed to provide a memory map of a file that already exists, and is not being modified.
If you want to use a file that is being modified, then you shouldn't use <code>mmap</code>.

