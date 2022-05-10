import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Results in the following exception:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect the <code>ValueError</code> to be raised only after the <code>a = m[:]</code> attempted to read from <code>m</code> since <code>m</code> is just a view of the file's contents.
I've done some digging and it appears that <code>mmap.mmap</code> is using the <code>lseek</code> function to establish the position of the <code>mmap</code> object (in this case 0). The documentation for <code>lseek</code> says that the position of the file is updated but only if the file is open for writing.
The <code>mmap</code> object is constructed in the <code>mmap.py</code> file in the Python's source code.
<code>m = mmap.mmap
