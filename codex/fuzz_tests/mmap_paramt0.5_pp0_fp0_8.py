import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
    m.close()
</code>
It works fine on Linux, but on Windows it prints <code>1</code> instead of <code>2</code>.
What's the problem?


A:

I think this is an issue with the <code>mmap</code> implementation on Windows.
It's not clear from the documentation whether <code>mmap.mmap</code> is supposed to be able to write to a file opened in read-only mode, but it seems to work fine on Linux.
If you open the file in read-write mode, it works fine:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
    m.close()
</code>

