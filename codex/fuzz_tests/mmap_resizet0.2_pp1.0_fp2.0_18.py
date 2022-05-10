import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expect the output to be <code>b'\x01'</code>.
Why does this happen?


A:

The mmap object is not updated when you truncate the file. You can see this if you print the length of the mmap object:
<code>print(len(m))
</code>
This will print <code>1</code> even after truncating the file.
You can update the mmap object by calling the <code>resize</code> method:
<code>m.resize(0)
</code>

