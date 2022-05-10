import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line fails with:
<code>Traceback (most recent call last):
  File "mmap.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
But if the file is opened in read-only mode, it succeeds:
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would like to be able to truncate the file and then read from the <code>mmap</code> object. Is this possible?


A:

The <code>mmap</code> object does not have any kind of reference to the file object you used to create it.  It's just a view into the memory that the file is mapped to.  If you truncate the file, the memory that used to contain the contents of the file is no longer mapped to it.
This is why you can't open the file in read-only mode and then truncate
