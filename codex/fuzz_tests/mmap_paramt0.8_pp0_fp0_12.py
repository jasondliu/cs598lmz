import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = chr(2)

with open('test', 'rb') as f:
    print bin(ord(f.read(1)))
</code>


A:

<code>bytes(1)</code> creates a <code>bytes</code> object in Python 3, which is basically the same as <code>str</code>. But the <code>mmap</code> module doesn't allow you to write a string to it, only a <code>bytes</code> object. In Python 2, <code>bytes(1)</code> would create a <code>bytes</code> object with length 1, but in Python 3, it creates a <code>bytes</code> object with the character whose numeric value is <code>1</code>, which is the ASCII character <code>SOH</code> (start of heading). So, you're writing the character <code>SOH</code> to the file. The corresponding <code>ord(f.read(1))</code> is 1, which is <code>0b1</code>.

