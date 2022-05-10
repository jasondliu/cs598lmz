import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I would expect this to print <code>b'\x00'</code>. However, it prints <code>b'\x01'</code>.
My question is: why does this happen?
I know that if I change the <code>f.truncate()</code> line to <code>m.resize(0)</code>, then it would print <code>b'\x00'</code>. I am curious why this is the case, because <code>m.resize(0)</code> seems to do more than just truncating the file. I read that it deletes the mapping, but I don't understand why that would change the result.


A:

The <code>mmap</code> object has a <code>MAP_SHARED</code> flag set by default, which means that the memory map is shared with other processes that have the same file open.
In your case, the file is truncated by the <code>truncate()</code> method, so the memory map is updated to reflect the new size. But when you
