import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(len(a))
</code>
The output is <code>1</code>, which is what I expected.
However, if I change the code to:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = m[:]
    print(len(a))
</code>
The output is <code>0</code>.
Why does closing the mmap object change the behavior of the slice operation?
I'm running Python 3.5.2 on Windows 10.

