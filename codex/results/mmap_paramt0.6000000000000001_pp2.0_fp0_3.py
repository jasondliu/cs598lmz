import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(1))
</code>
I get the error: <code>TypeError: write_byte() takes exactly 1 argument (2 given)</code>
What am I doing wrong?


A:

<code>m.write_byte(bytes(1))</code> is <code>m.write_byte(1)</code>
<code>bytes(1)</code> is just <code>1</code>

