import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
It gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the problem is that I truncate the file after creating the mmap object. But I need to do it this way. Is there any way to solve this problem?


A:

You can't use <code>mmap</code> on a file that has been truncated to zero.
You can use <code>mmap</code> on a file that has been truncated to a non-zero size.
You can use <code>mmap</code> on a file that has been extended.
You can use <code>mmap</code> on a file that has been extended and then truncated.
You can't use <code>mmap</code> on a file that has been truncated to zero.

