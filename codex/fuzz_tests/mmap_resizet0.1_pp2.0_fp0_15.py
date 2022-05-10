import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I thought that the mmap would be able to read the data that was there before the truncate.
Is there a way to do this?


A:

The <code>mmap</code> object is tied to the file descriptor, not the file object.  The file descriptor is not affected by the <code>truncate</code> call.  The <code>mmap</code> object is still pointing to the original file size.
You can use <code>os.ftruncate</code> to truncate the file descriptor.
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m =
