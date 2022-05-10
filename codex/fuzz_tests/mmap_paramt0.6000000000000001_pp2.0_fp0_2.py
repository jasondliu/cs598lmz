import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[:] = b'\x00'
</code>
This results in the following error:
<blockquote>
<p>AttributeError: type object '_io.BufferedReader' has no attribute 'fileno'</p>
</blockquote>
I understand that in order to use <code>mmap</code> the file needs to be opened in binary mode, but what exactly is the difference between <code>rb</code> and <code>r+b</code>?

