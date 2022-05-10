import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m.close()
</code>
The code above will print a memory map object like this:
<code>&lt;mmap.mmap object at 0x7fb8c4f4a1d0&gt;
</code>
The <code>mmap</code> module also has a <code>mmap.error</code> class and a <code>mmap.ALLOCATIONGRANULARITY</code> constant. But there are no other classes or constants in the module. I have found this page in the docs, but it only tells me how to use <code>mmap</code> to open a file or find the page size of the system.
I have also searched all the <code>.so</code> files in <code>/usr/lib</code> and <code>/usr/local/lib</code> for a symbol named <code>mmap</code> or <code>MMAP</code>, but found nothing.
I have searched the source code of Python 3.6.2 and found out that the implementation of the <code>mmap</code> module is
