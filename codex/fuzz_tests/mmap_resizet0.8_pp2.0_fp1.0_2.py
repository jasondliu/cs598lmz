import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code gives no warnings and produces <code>a</code> equal to <code>b''</code>, which is not what I want.
The question is whether I can be sure that <code>m[:]</code> is not reading past the end of the file in Python 2.7.
I saw the question:
Mmap and truncate on Python. The last sentence of the answer states "If the file was opened with write access, you can truncate the mapping with a call to truncate() on the file object."
I tried <code>f.truncate()</code> but it did not work.

The code is just an example. The code below is better:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0, 2)
    pos = m.tell()
    f.truncate()
    a = m[:pos]
</code>

I am using Python 2.7.


A:

I have replicated your example as follows:
<code
