import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I expect that <code>a</code> will be <code>bytes(1)</code>.
What is the correct way to use <code>mmap</code> with <code>truncate</code>?


A:

You can't use <code>mmap</code> on a file that has been truncated.
<blockquote>
<p>The file must not be smaller than size. If the file is larger than size, the extra data is ignored. If the file is smaller than size, it is extended, and the extended part reads as null bytes ('\x00').</p>
</blockquote>
You can't use <code>mmap</code> on a file that has been truncated.

