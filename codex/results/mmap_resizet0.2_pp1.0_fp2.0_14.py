import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the mmap object is not aware of the truncation, but is there a way to make it aware?
I could close the mmap object and reopen it, but I'd like to avoid that.
I could also reopen the file, but I'd like to avoid that as well.
I could also use <code>m.resize()</code>, but I'd like to avoid that as well.
I could also use <code>m.seek()</code> and <code>m.read()</code>, but I'd like to avoid that as well.
I could also use <code>m.tell()</code> and <code>m.read()</code>, but I'd like to avoid that as well.
I could also use <code>m.read()</code> and <code>m.seek()</code>, but I'd like to avoid that as well.
I could also use <code>m.read()</code> and <code>m.tell()</code>, but I'd like to avoid
