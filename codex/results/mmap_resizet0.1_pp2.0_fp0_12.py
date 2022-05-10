import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>
I would expect the output to be <code>b''</code>
Why is this?


A:

The <code>mmap</code> object is not updated when you truncate the file.  It still thinks the file is the same size it was when you created the <code>mmap</code> object.  You can see this by printing the <code>mmap</code> object's <code>size</code> attribute:
<code>&gt;&gt;&gt; m.size
1
</code>
If you want to update the <code>mmap</code> object, you need to call <code>mmap.resize</code>:
<code>&gt;&gt;&gt; m.resize(0)
&gt;&gt;&gt; m.size
0
</code>

