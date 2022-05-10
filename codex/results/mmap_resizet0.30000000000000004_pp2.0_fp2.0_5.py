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
I would expect <code>a</code> to be <code>b''</code> since the file is empty.
I'm using Python 3.6.4 on macOS 10.13.4.


A:

The problem is that you are creating a memory map of the entire file, but then truncating the file.  The memory map is still pointing to the same place, but there is no data there.  You can fix this by creating the memory map after you truncate the file.
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>

