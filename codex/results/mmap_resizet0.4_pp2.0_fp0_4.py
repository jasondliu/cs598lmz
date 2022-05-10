import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
The output is <code>b''</code>. 
The question is: why does the <code>mmap</code> object still contain data after truncating the file?


A:

The <code>mmap</code> object still contains data because it is a view into the file, not the file itself.  It doesn't know that the file was truncated, so it doesn't do anything special.  The file was truncated, but the <code>mmap</code> object still has a view into the file, and that view is still valid.  The data is still there.  It just happens to be zero bytes.
If you want to clear the data in the <code>mmap</code> object, you need to write to it.  You can do that with <code>m.write(b'\x00')</code> or <code>m.write_byte(b'\x00')</code>.  Or you can use <code>m.resize()</code> to resize the <code>mmap</code> object, which will
