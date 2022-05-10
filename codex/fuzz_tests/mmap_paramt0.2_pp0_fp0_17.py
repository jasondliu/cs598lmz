import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This works fine on Linux, but on Windows, I get the following error:
<code>WindowsError: [Error 87] The parameter is incorrect
</code>
What am I doing wrong?


A:

You need to specify the length of the file when creating the <code>mmap</code> object.
<code>m = mmap.mmap(f.fileno(), 1)
</code>

