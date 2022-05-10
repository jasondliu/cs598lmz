import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error: <code>ValueError: mmap closed or invalid</code>. Is there any way to make this work?


A:

Do <code>f.seek(0)</code> and <code>m.seek(0)</code> before truncating the file.

