import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is empty, because <code>truncate</code> just decreases the file size, but doesn't clear the data.
Using <code>seek()</code> is not a solution.
Is there a way to perform the truncate() faster? (without reading all the file and writing it again)


A:

You can use the <code>os</code>-specific APIs to truncate a file, e.g. for POSIX you can use the <code>os.ftruncate</code> function.
This is not specific to <code>mmap</code>; it applies to any file.

