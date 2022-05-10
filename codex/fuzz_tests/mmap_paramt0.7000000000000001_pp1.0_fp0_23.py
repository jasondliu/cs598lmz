import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE,
                  offset=0,
                  prot=mmap.PROT_WRITE)
    # m[0] = b'b'
    m.write(b'b')

m.close()
</code>
But in this case, if I write:
<code>m[0] = b'b'
</code>
then I get error:
<code>TypeError: 'bytes' object does not support item assignment
</code>
Why?


A:

From the docs:
<blockquote>
<p>mmap objects support the buffer interface (Python 2.6 and higher);
  read-only buffers cannot be exported</p>
</blockquote>
So you can't modify the memory map via the buffer interface.

