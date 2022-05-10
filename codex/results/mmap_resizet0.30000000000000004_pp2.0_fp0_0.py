import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints <code>b'\x00'</code> which is not what I expected.
What I expected is that <code>m[:]</code> would raise an exception because the file was truncated.
What is the correct way to check if the file was truncated?


A:

The <code>mmap</code> object is not aware of the file size. It only knows the size of the memory map.
You can check the file size by calling <code>m.size()</code>.

