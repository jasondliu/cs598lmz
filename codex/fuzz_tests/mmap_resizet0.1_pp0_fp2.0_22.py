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
I understand that the mmap is pointing to a location that no longer exists, but I don't understand why.  I thought that the mmap would be updated to point to the beginning of the file.  Is there a way to do this?


A:

The <code>mmap</code> object is not updated when the file is truncated.  It is still pointing to the same location in the file, which is now beyond the end of the file.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object to match the new size of the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.res
