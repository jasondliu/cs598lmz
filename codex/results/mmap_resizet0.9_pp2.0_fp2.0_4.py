import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # error here
    m.close()
</code>
If we put <code>f.close()</code> before <code>m[:]</code>, the error occurs at <code>f.close()</code> line.
Why does this error occur?

