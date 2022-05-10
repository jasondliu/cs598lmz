import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(m[:])
print(a)
</code>
The output is:
<code>b''
b'\x00'
</code>
Why does <code>m[:]</code> return an empty string, and not the same empty string that <code>m.read()</code> returns? What's the difference?


A:

A Python 3 <code>bytes</code> object contains only objects of type <code>int</code> (and these are interpreted as unsigned-char).
In Python 2, a <code>str</code> is a sequence of bytes (like a <code>bytes</code> or <code>bytearray</code> in Python 3).
You seem to be making the mistake that the output of <code>print</code> is the same as the value. <code>print</code> is used to output a representation of the value, which may or may not reflect the value its self.
In Python 2, a <code>str</code> with the only character being a NUL byte is printed as an empty string. The same happens for <code>bytes</code> objects
