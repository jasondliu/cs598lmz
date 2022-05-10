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
Output:
<code>b'\x00'
</code>
Why it happens?


A:

<code>a = m[:]</code> simply copies everything in the memory map into <code>a</code>.  This is what you would expect it to do.
I'm not sure what you expect to see in <code>a</code> after you truncate the file.  The memory map is still there, but it's only as large as the file was before you truncated it.  If you want to see what's actually in the memory map, try <code>print(m[:])</code>.  Or, even better, try <code>print(m.read())</code> (or <code>.read(1)</code>), and you'll get a clearer idea of what's going on.
(Note: you should probably also add <code>m.seek(0)</code> immediately after truncating the file, before you try to read from it.)

