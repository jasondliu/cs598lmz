import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
How can I get the data from the file?


A:

The <code>mmap</code> object is tied to the file descriptor, not the file object.
When you truncate the file, the file descriptor is still valid, but the file object is no longer valid.
You can't use the <code>mmap</code> object after truncating the file.

