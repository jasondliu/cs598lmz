import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
The output is <code>b'\x01'</code>, despite the fact that the file is empty.
In fact, if I try to <code>f.write</code> anything, I get a <code>ValueError</code> saying <code>mmap invalid</code>.
However, if I only read from the mmap, the file is empty.
I'm using Python 3.4.3 on Linux, but I observed the same behaviour on Windows.
Why is this happening? Is this the expected behaviour?


A:

The behaviour you're observing is expected. The file pointer for <code>f</code> is at the end of the file, so <code>f.write</code> fails, because you're trying to write at an invalid position.
You can move the pointer back to the start of the file:
<code>f.seek(0)
f.write(b'a')
</code>
The reason why <code>m</code> still shows the old data is because <code>mmap</code> doesn't update the data automatically.
You can update
