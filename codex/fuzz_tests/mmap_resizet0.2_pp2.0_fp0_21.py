import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I know that I can use <code>mmap.resize</code> to resize the file, but I want to know why the file is truncated.


A:

The <code>mmap</code> object is a view of the file.  When you truncate the file, the view is no longer valid.  The <code>mmap</code> object is not updated when the file is truncated.  You can see this by printing the length of the <code>mmap</code> object:
<code>print(len(m))
</code>
This will print <code>1</code> even after the file is truncated.

