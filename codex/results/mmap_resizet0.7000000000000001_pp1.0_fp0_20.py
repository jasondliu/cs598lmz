import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux.
But on Windows it raises an <code>EOFError</code> exception.


A:

The <code>mmap</code> object is no longer valid after you truncate the file.
From the <code>mmap</code> docs:
<blockquote>
<p>Operations on a <code>&lt;code&gt;mmap&lt;/code&gt;</code> object may raise the <code>&lt;code&gt;WindowsError&lt;/code&gt;</code> exception, although
  most calls on Windows will not. Windows will sometimes raise an
  <code>&lt;code&gt;InvalidHandle&lt;/code&gt;</code> exception when the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object must be closed. This can
  happen when the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object must close the handle to the underlying file,
  and the file was opened without <code
