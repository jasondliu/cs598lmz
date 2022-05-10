import mmap
# Test mmap.mmap()

import mmap

def write_mmap(m):
    m[1:3] = b"\x00\xff"

def write_file(f):
    f.seek(1)
    f.write(b"\x00\xff")

with open("foo.txt", "w+") as f:
    f.write("Hello world!")
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    write_mmap(m)
    write_file(f)
    print(m.read())
</code>
But the result is:
<code>Hello world!��
</code>
I expected:
<code>Hello��world!
</code>
I don't know why.


A:

From the docs:
<blockquote>
<p>Memory-mapped files are created using the <code>&lt;code&gt;mmap&lt;/code&gt;</code> module. <strong>To create a
  memory-mapped file object
