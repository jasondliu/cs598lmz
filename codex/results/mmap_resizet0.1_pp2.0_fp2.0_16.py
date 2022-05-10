import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> object to be updated when the file is truncated.
Is there a way to make this work?


A:

You can't use <code>mmap</code> on a file that has been truncated.
<code>mmap</code> is a memory-mapped file, which means that the file is mapped into memory.  If you truncate the file, the memory is no longer mapped to the file.

