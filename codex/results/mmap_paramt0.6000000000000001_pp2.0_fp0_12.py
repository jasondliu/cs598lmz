import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
This prints <code>b'\x02'</code> but I expected <code>b'\x01'</code>.
Why does this happen?
I can't find anything about this in the documentation.


A:

The reason for this behaviour is that the file is opened with <code>'r+b'</code>, which means that the file is opened for both reading and writing.
When you open a file for reading and writing, that file is positioned at the end of the file.
So, when you write a byte using the mmap, it is written at the end of the file, and the original byte is left untouched.
This can be verified using <code>os.lseek()</code>:
<code>&gt;&gt;&gt; import os
&gt;&gt;&gt; fd = os.open('test', os.O_RDWR)

