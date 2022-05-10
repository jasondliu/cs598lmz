import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
I get <code>b'\x02'</code> and not <code>b'\x01'</code>.
I've also tried with <code>mmap.ACCESS_WRITE</code> and <code>mmap.ACCESS_COPY</code> instead of <code>0</code> but I still get the same result.
What am I doing wrong?
I'm using Python 3.4.4 on Windows 10.
Thank you for your help.


A:

You are changing the value of the <code>bytes</code> instance, not the mapping:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(b'1')
...
1
&gt;&gt;&gt; with open('test', 'r+b') as f:

