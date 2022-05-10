import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(a)
</code>
The above code returns <code>b'\x01'</code> as expected
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
print(a)
</code>
But this returns <code>b''</code>
So I want to ask:

Is it possible to resize the file with mmap module? I ask this because I found this in the docs:

<blockquote>
<p>The underlying file may be resized at any time, independently of the
  mmap object.  This may cause the values of various mmap attributes to
  change, including the size and location of the buffer in memory.</p>
</blockquote>

Why does truncate work but resize doesn't? mmap is supposed to be a wrapper for the underlying file.

Thanks!


A:
