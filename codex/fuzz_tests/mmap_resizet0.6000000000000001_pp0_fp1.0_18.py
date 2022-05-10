import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This will raise an exception on the last line, but it is not the exception I would expect:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m.close()
ValueError: mmap closed or invalid
</code>
I would expect an <code>mmap.error: cannot resize a file mapping object</code> exception.
What is happening here?


A:

The <code>mmap</code> module is built on top of operating system facilities, and the details of how it works vary from operating system to operating system.
On Linux, a <code>mmap</code> is just a mapping of a file descriptor to a region of memory. The file descriptor is the key that the operating system uses to locate the file, so if you close the file descriptor, the mapping is broken.
On Windows, a <code>mmap</code> is a mapping of a file name to a region of memory. When you truncate the file, you change the size of the file, which means that the mapping is no
