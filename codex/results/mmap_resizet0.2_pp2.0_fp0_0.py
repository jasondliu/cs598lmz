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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I understand why this is happening, but I don't know how to fix it. I need to truncate the file, but I also need to keep the mmap object around. I've tried calling <code>m.resize()</code> and <code>m.close()</code> after truncating the file, but neither of those seem to work.
Is there a way to truncate the file and keep the mmap object around?


A:

The problem is that you are trying to access the memory map after you have truncated the file.  The memory map is no longer valid.  You need to close the memory map before truncating the file.

