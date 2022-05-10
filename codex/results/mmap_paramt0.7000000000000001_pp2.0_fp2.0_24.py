import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))

with open('test', 'r+b') as f:
    print(f.read())
</code>
I expect to read <code>b'\x02'</code> when I open the file again, but I get <code>b'\x01'</code>.


A:

You need to close the mmap before trying to read the file again. 
From the docs:
<blockquote>
<p>Python automatically performs <code>&lt;code&gt;mmap.close()&lt;/code&gt;</code> when the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is garbage collected, but you may do it manually if you wish. <strong>You must do this explicitly, or else changes you make to the mmap object may not show up in the file</strong>. (This is because closing the mmap object flushes any unwritten changes to disk.)</p>
</blockquote>

