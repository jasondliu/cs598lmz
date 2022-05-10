import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect that the mmap object would be updated when the file is truncated.
Is there a way to truncate a file and have the mmap object updated?


A:

I'm not sure why you would expect the mmap object to be updated when the file is truncated.  The mmap object is a view into the file, and the file is not truncated until the <code>truncate()</code> call.  The mmap object is not a view into the file descriptor, it's a view into the file itself.

