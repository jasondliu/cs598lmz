import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'

with open('test', 'rb') as f:
    print(f.read())
</code>
The problem is that the file is not modified. If I open it with VIM, it says "File was changed on disk; what do you want to do? Edit anyway, reload (overwrite changes)". If I choose "Edit anyway" and save the file, the modification is applied.
I have tried the same code with Python 3.4.3 and 3.4.4 on Ubuntu 15.10 and it worked.


A:

That's the expected behavior of <code>mmap</code> on Windows.
The <code>mmap</code> module documentation states:
<blockquote>
<p>On Windows, changes to a file <em>not</em> opened for reading and writing may not be visible to other processes until the <code>&lt;code&gt;FlushFileBuffers()&lt;/code&gt;</code> function is called, or the file handle is closed.</p>
</blockquote>

