import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When I run this, I get a <code>ValueError: mmap offset is greater than file size</code>. I understand that this is because the file was truncated, but I don't understand why this is happening.
I thought that since I had already opened the file, the <code>mmap</code> would know that it was truncated and adjust the offset accordingly. But apparently this is not the case.
I know that I can get around this by simply not truncating the file, but that's not what I want to do. I am truncating the file and then I want to read the contents of the file up to the point it was truncated.
Is there a way to do this?

