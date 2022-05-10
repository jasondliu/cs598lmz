import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Causes the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
In the above example, is there any way to reduce the required code to only:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>


A:

What you're doing here is creating a memory map for a file that doesn't exist. Since you've opened the file for reading and writing, python creates the file for you. You then truncate the file to 0 bytes and try to read from it.
You can prevent this by passing <code>mmap.MAP_PRIVATE</code> as the <code>flags</code> argument to <code>mmap.mmap</code>. The private flag means that the memory map will not be written back to the file. 
<code
