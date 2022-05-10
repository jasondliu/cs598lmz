import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I expect to get <code>b'\x01'</code> but I get <code>b''</code>.
I know that if I do <code>m.seek(0)</code> before <code>a = m[:]</code> I get the expected result.
Why is this happening?
I am using Python 3.6.5 and the <code>mmap</code> module on Windows 10.


A:

The mmap object is a window into the file, not a copy of the file's contents.  Once it's been truncated, the mmap object is no longer a window into the file.
If you want to get the data from the file, you need to re-open the file and read it.

