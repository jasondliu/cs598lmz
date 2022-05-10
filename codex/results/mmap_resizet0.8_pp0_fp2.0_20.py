import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected <code>a</code> to be an empty string, but it equals <code>b'\x01'</code>. Why is that so?


A:

The problem is that <code>fileno</code> returns the file descriptor for the current position. So, if you truncate the file at a position which is not the beginning of the file, you are effectively truncating the file before the position of the file descriptor.
The docs explain this, but the explanation is kind of poor.
<blockquote>
<p>You can open files in a mode that allows you to read and write existing data, but prevents you from truncating (resizing) the file, either deliberately or by writing past the end of the file. You can also open files in a mode that allows you to both read and write existing data, and also to truncate the file by writing past the end of the file.</p>
</blockquote>

