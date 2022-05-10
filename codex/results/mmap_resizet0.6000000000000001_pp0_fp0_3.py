import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.flush()
    m.close()
    print(a)
</code>
The output is <code>[1]</code> although it should be <code>[]</code> because the file is truncated.
How can I make the contents of the <code>mmap</code> reflect the changes made to the underlying file?


A:

There is a <code>resize</code> method for the <code>mmap</code> object, which will resize the mapped region to match the underlying file size.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    m.flush()
    m.close()
    print(a)
</code>

