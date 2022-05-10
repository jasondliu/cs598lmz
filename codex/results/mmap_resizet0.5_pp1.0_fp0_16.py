import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would have expected <code>a</code> to be the empty bytes object, but it is actually <code>b'\x01'</code>.
I am using Python 3.6.4 on Linux (4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux).
Is this a bug? If not, how can I get the expected behavior?


A:

This is a bug in Python 3.6.4. I have just tried the same code on Python 3.7.2 and it works as expected.

