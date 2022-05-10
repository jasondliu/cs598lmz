import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When I run this code, I get the following error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I don't understand why the offset is greater than the file size. I thought that if I truncate the file, the offset would be updated.


A:

The <code>mmap</code> object is not aware of changes to the file size. You need to call <code>mmap.resize</code> to update the size of the memory map.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
</code>

