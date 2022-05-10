import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: mmap can't enlarge memory maps on this system</code> on the last line.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are trying to read from the memory map after truncating the file.
The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The size of the mapped region must not be zero, and the region must
  fit within the mapped file. If the file is larger than the requested
  size, the extra data is ignored. If the file is shorter than the
  requested size, only the initial part of the file is mapped (the
  file is not extended).</p>
</blockquote>
So, when you truncate the file, the memory map is no longer valid.

