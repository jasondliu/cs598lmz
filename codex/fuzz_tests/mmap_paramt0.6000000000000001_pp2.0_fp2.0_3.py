import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'

with open('test', 'rb') as f:
    print(f.read())
</code>
It prints <code>b'0'</code> instead of <code>b'\x00'</code>. Also, if I try to change the first byte to <code>b'\x01'</code>, it writes <code>b'\x01'</code> to the file instead of <code>b'\x01'</code>.
Why does it do that?


A:

<code>bytes()</code> creates a bytes object with a given length, so <code>bytes(1)</code> creates a bytes object of length 1, with all the bytes initialized to 0.
But <code>b'0'</code> is a bytes object of length 1, which contains the byte <code>0x30</code>, which is the ASCII value for '0' (the character 0).
So, when you try to write <code>b'0'</code> to the file, it writes the character '0', which is what you're
