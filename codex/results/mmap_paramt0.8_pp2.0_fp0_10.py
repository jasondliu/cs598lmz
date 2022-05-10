import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    r = f.read()
    print(r)
</code>
However, the result is like if I had only changed the last byte.


A:

You need to specify the file size when you mmap it. 
As you can't know the size when you open the file, you need to temporarily mmap it using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code>, then call <code>.write()</code> on it, then <code>.seek()</code> to the end of the file and call <code>.write()</code> to add a new byte and then mmap it again this time with a size of <code>mmap.mmap(f.fileno(), f.tell())</code>.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f
