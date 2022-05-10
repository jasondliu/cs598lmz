import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    del m
    b = f.read()
</code>
On OSX and Linux <code>a</code> is <code>b''</code> and <code>b</code> is <code>b''</code>. On Windows <code>a</code> is <code>b'\x00'</code> and <code>b</code> is <code>b''</code>.
In this example the data is not truncated until the <code>mmap</code> object is deleted.
If I use <code>m.flush()</code> it does not help.
If I use <code>m.close()</code> the data is truncated.
If I use <code>del m</code> it does not help.
If I use <code>m = None</code> it does not help.
I also tried using <code>os.ftruncate</code> instead of <code>f.truncate</code> but I got the same results.
So my question is: what is the correct way to truncate a file while still having an open <code>mmap</
