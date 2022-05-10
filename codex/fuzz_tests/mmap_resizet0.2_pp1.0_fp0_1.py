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
I expected it to be <code>b'\x01'</code>.
Why is this?


A:

The <code>mmap</code> object is not updated when the file is truncated.  You can see this by printing the length of the <code>mmap</code> object:
<code>&gt;&gt;&gt; len(m)
1
</code>
You can force the <code>mmap</code> object to be updated by calling its <code>resize</code> method:
<code>&gt;&gt;&gt; m.resize(0)
&gt;&gt;&gt; len(m)
0
</code>

