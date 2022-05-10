import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The above example gives the following trace:
<code>  File "mmap.py", line 16, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
A more complex example:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize((1000,))
    m[0] = bytes(1)
    m.close()
</code>
The above example gives the following trace:
<code>  File "mmap.py", line 13, in &lt;module&gt;
    m.resize((1000,))
ValueError: new size cannot be greater than file size
</code>
The same goes for <code>mmap.resize</code>, which is meant to change the size of the mapping.
