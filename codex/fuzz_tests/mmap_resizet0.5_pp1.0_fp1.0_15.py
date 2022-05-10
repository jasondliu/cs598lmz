import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>
The problem is, that the file size is 0, but the offset is still 1.
The documentation says:
<blockquote>
<p>If length is 0, the maximum length of the map is the current size of the file when mmap is called. </p>
</blockquote>
But this doesn't seem to be the case.
If I change the code to:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.seek(0, os.SEEK_END)
    f.truncate()
    a = m[:]
    m.close()
</code>
It works. But I don't know if this is a bug or a feature.
Can anyone explain this behaviour?

