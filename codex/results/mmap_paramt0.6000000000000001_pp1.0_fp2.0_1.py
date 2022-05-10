import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(3)
    m.write_byte(bytes(1))
    m.write_byte(bytes(1))
    m.seek(0)
    print(m.read(3))
    m.close()
</code>
prints <code>b'\x01\x00\x00'</code>
But I expected <code>b'\x01\x01\x01'</code>.
How can I write to the new space?


A:

<code>mmap.write_byte</code> takes an <code>int</code> parameter, not a <code>bytes</code> object.
From the docs:
<blockquote>
<p><code>&lt;code&gt;mmap.write_byte(byte)&lt;/code&gt;</code></p>
<p>Write a byte to the current position in the mapped area. <strong>The byte must be an integer between 0 and 255.</strong></p>
</blockquote>
(Emphasis mine)
Your code is trying to write the bytes <code
