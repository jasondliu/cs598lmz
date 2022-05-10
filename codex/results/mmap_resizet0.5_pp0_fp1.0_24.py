import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I have a file <code>test</code> with 1 byte in it. I open it and create a memory map. I then truncate the file to 0 bytes. Then I read the memory map.
The result is (on Linux, Python 3.6):
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read memory mapped array: invalid pointer
</code>
Why is this happening? The file has been truncated to 0 bytes. The memory map should be empty. But the memory map is still trying to read from the old location.
I am aware that I could just use <code>m.resize</code> instead of <code>f.truncate</code>. But I am curious why this is happening.
I am also aware that I could just ignore the error, and the memory map will be empty. But I am curious why the memory map is not empty right away.


A:

The <code>mmap</code> module's documentation for <code>mmap.mmap
