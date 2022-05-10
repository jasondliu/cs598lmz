import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'0')

with open('test', 'rb') as f:
    print(f.read())
</code>
The read returns <code>b'0'</code> instead of <code>b'1'</code>. Why is that? How do I get <code>b'1'</code> with the <code>mmap</code> module?
(This question is an extension of Overwriting the first byte in a file with zero with mmap).


A:

You are getting <code>'0'</code> because you are writing <code>'0'</code>.
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
</code>
So, when you write <code>b'0'</code>, you are overwriting that byte with the byte for the single character <code>'0'</code>.
If you do <code>bytes(1)</code> again, you'll see that it is a single-byte string containing the byte for <code>'\x00'</code>, which is
