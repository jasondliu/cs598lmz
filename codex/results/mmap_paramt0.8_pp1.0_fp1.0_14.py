import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = b'\n'
</code>
The code above works as expected. The documentation states:
<blockquote>
<p>The actual behaviour depends on the <code>&lt;code&gt;length&lt;/code&gt;</code> argument: if less then the
  current size of the underlying file it is equivalent to <code>&lt;code&gt;mmap(fileno,
  length, access[, flags])&lt;/code&gt;</code> otherwise it is equivalent to <code>&lt;code&gt;mmap(fileno, 0,
  access[, flags])&lt;/code&gt;</code>; the actual size of the memory map, and the file offset
  used for <code>&lt;code&gt;mmap()&lt;/code&gt;</code>, are adjusted to reflect the current size of the
  underlying file.</p>
</blockquote>
It seems the <code>length</code> argument is ignored if the file size is smaller (which is the case here).
What's the point
