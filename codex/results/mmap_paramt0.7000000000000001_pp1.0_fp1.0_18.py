import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    print(m[0])
    f.write(bytes(2))
    print(m[0])
</code>
I want to know, how exactly is it possible?
I tried to do something similar with <code>ctypes</code>, but I haven't found a way to access the memory from the file.
The documentation says:
<blockquote>
<p>Note that modifications to the file itself are not allowed through the
  mmap object. In some cases, you can use msync() to force the changes
  made to the mmap’ed region to disk.</p>
</blockquote>
But I am not even trying to modify the file and get the changes from mmap, I am just trying to get the changes from the file and get them with mmap.

