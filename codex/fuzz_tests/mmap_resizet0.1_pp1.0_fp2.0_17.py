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
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I thought that the mmap would be updated to reflect the new file size. Is there a way to do this?


A:

The <code>mmap</code> object is not updated when the file is truncated. You need to <code>close</code> the <code>mmap</code> object and then reopen it.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

