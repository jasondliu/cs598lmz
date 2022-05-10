import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
This code prints <code>b''</code> on Python 3.4.3, but <code>b'\x00'</code> on Python 2.7.8.
Why does this happen?


A:

<code>mmap</code> is a bit of a black box. It allocates a region of memory and maps it to a file. The memory region is not necessarily initialized to anything, and <code>mmap</code> does not take any steps to ensure that it is.
When you truncate the file, you're not truncating the memory region that <code>mmap</code> allocated. <code>mmap</code>'s view of the file is not updated, and it will happily read beyond the end of the file.
If you want to ensure that the file is initialized to something, you can use <code>os.ftruncate</code> to set the file size before calling <code>mmap</code>:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

