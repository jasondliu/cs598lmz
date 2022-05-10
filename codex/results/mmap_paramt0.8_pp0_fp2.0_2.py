import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
Is there a way to do this using a temporary file on the filesystem?
Note that this is a simplified example to demonstrate the issue. The real code is opening a file for writing and then applying a diff to it using memory mapping. The file is read-only during the diffing part, and it is <code>os.rename()</code>'d to the desired final name after the diff is complete.


A:

<blockquote>
<p>Is there a way to do this using a temporary file on the filesystem?</p>
</blockquote>
No, you have to use some form of in-memory storage, like <code>mmap(..., MAP_PRIVATE)</code>.

