import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'
    m.close()
</code>
This works as expected, and the byte is changed to <code>1</code>.
However, if I change the <code>b'1'</code> to <code>b'2'</code>, the byte is changed to <code>\x02</code> instead of <code>2</code>.
Why is this?


A:

<code>mmap</code> is a binary interface. The <code>mmap</code> object represents the file as a sequence of bytes.
<code>b'2'</code> is a single-element <code>bytes</code> object. It contains the byte <code>0x32</code>.
<code>b'1'</code> is a single-element <code>bytes</code> object. It contains the byte <code>0x31</code>.
<code>b'2'</code> is not the same as <code>b'1'</code>, any more than <code>b'a'</code> is the same as <
