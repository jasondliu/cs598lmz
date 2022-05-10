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
It prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I've tried to use <code>m.resize(len(a))</code> and <code>m.resize(f.tell())</code> but it didn't help.
I've also tried to use <code>mmap.ACCESS_READ</code> instead of <code>mmap.ACCESS_WRITE</code> but it didn't help too.
I'm using Python 3.5.2.


A:

The problem is that the file descriptor of the file is still open, and your <code>mmap</code> object is still referring to it. 
The <code>mmap</code> object is not aware that the file was truncated. 
When you do <code>m[:]</code>, the <code>mmap</code> object is using the file descriptor to read the file, and it is reading the current content of the file, which has been truncated to 0 bytes.

