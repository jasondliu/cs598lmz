import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get:
<code>b'\x00'
</code>
If I change the file to be written with <code>0</code> instead of <code>1</code>, I get:
<code>b''
</code>
So, I can only read the first byte, and I can't read the last byte.

I want to be able to read the full contents of the file, even if I'm truncating it.
I'm using Windows 10, and Python 3.6.1.
I'm using the <code>mmap</code> module to create a memory-mapped file, and then I'm truncating the file. I then want to be able to read the full contents of the file, even though I've truncated it.
I can't do <code>m.seek(0, os.SEEK_END)</code> because I'm truncating the file.
I can't do <code>m.seek(0, os.SEEK_SET)</code> because I'm truncating the file.
I can't do <code>m.seek(0
