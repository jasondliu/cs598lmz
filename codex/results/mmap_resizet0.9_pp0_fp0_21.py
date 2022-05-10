import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
</code>
results in <code>IndexError: mmap index out of range</code>.
And
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    del m[:]
    f.truncate()
    a = m[:]
    b = m[:]
</code>
results in <code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: expected LP_c_byte instance instead of c_size_t</code>.
Without truncation, reading from the mmap produces the bytearray, deleting the mmap and reading from it again results in <code>IndexError: mmap index out of range</code>.
The relevant section in the <code>mmap</code> docs is
<blockquote>
<p>If size is larger than current buffer, it will be resized to contain the entire length
