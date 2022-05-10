import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b'\x01'
</code>
If I change the file mode to <code>r</code> instead of <code>r+b</code>, it will give me the correct output:
<code>with open('test', 'r') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
</code>
Output:
<code>b''
</code>
Why does the file mode matter?


A:

The file is opened for writing, and you truncate it, so it no longer has any data. You then open the memory mapped file. You get the data from there.
If you open the file for reading, it is not possible to truncate it, and so you get the data you expect.
<code>m[:]</code> will return an empty byte string.

