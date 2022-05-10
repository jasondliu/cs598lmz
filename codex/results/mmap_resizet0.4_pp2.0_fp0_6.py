import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code works fine and prints <code>b'\x01'</code>.
However, if I change <code>f.truncate()</code> to <code>f.truncate(0)</code>, I get <code>mmap.error: [Errno 22] Invalid argument</code>.
Why is it so?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The size argument specifies the initial size of the mapped region. If
  size is larger than the file’s current size, the file is extended to
  contain size bytes. The contents of the new area are unspecified.</p>
</blockquote>
So, when you create the <code>mmap</code> object, it extends the file to contain one byte. When you truncate the file to zero bytes, the <code>mmap</code> object is no longer valid.

