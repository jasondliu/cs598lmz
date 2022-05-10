import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord(b'1')
</code>


A:

The error arises from the fact that you overwrote the beginning of the file with a single character:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))
</code>
that results in a file size of 1 byte.
By opening the file in <code>'r+b'</code> mode, you give the <code>mmap</code> module the current size of the file. Since you did not change it, the <code>mmap</code> object points to the 1-byte-length file.
The following method updates the file and the <code>mmap</code> object:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    m[0] = ord(b'1')
</code
