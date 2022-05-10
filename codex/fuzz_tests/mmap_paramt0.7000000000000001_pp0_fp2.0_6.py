import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0], m[0] == 0)
    m[0] = 1
    m.close()
</code>
This code prints <code>1 False</code> which is unexpected as I'm changing the first byte of the file and then retrieving it.
This is on python 3.5.2, windows 10.


A:

The problem is that <code>bytes(1)</code> creates a <code>bytes</code> object of length 1 and with the value of the integer 1 in it. The integer 1 is the number 0x01 in hexadecimal.
<code>bytes(1)</code> is equivalent to <code>bytes([1])</code>.
You want to use <code>bytes([1])</code> or <code>bytes([0])</code>, depending on what you want to test for.
<code>bytes([1])</code> creates a <code>bytes</code> object with just one byte in it. The value of that byte is the integer 1, which is the number 0x01 in hexadecimal.

