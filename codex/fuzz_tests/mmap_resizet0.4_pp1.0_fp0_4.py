import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will print <code>b'\x00'</code>.
I'm using python 3.5.2 on Ubuntu 16.04.


A:

The documentation says:
<blockquote>
<p>The file’s size cannot be changed while mmap() is in use. To change the size of a file which is currently mapped in this way, close the mmap object, resize the file, and re-open the mmap object on the resized file.</p>
</blockquote>

