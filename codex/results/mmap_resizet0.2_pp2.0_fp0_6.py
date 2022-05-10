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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I don't understand why the offset is greater than the file size.
I'm using Python 3.5.2 on Windows 10.


A:

The problem is that you are using the <code>mmap</code> module incorrectly.
The <code>mmap</code> module is used to map a file into memory.  In your example, you are opening the file, then mapping it into memory, then truncating the file.  The file is now empty, but the memory map is still pointing to the old file contents.  When you try to access the memory map, it tries to access the old file contents, which are no longer there.
If you want to truncate the file, you need to do it before you map it into memory.  If you want to truncate the file after you map it into memory, you need to un
