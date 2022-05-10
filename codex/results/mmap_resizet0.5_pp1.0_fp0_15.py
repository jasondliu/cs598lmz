import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
</code>
I expect this to print <code>1</code>, but it prints <code>0</code>. Why?


A:

The <code>mmap</code> is not updated when you truncate the file.  You can see this by using the <code>tell</code> method of the mmap object:
<code>&gt;&gt;&gt; m.tell()
0
</code>
This shows that the mmap object is still at the beginning of the file, but the file has no content.  This is because the mmap object is a view of the file, rather than a copy of the file.  The mmap object is not updated when you truncate the file.  The mmap object is updated when you write to the file.
One way to fix this is to use the <code>close</code> and <code>mmap</code> methods of the file object:
<code>&gt;&gt;&gt; m.close()
&gt;&gt;&gt; m = f.mmap(0)
&gt;&
