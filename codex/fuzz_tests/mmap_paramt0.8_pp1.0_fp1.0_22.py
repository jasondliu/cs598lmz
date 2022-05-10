import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
    m.seek(0)
    print(m.size())
</code>
Result:
<code>1
0
</code>
We read <code>size()</code> in <code>read</code> mode, then switch to <code>read_write</code> and read it again. Note that without <code>seek(0)</code>, the second <code>size()</code> returns a negative number.
Now, how do I read the current position from an mmap? I tried <code>get_pos</code> and <code>tell</code> but they're not implemented on mmaps. I'm stuck.

