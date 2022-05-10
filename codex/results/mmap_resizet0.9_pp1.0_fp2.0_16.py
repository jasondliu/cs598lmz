import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
the output is: <code>Tcl_AsyncDelete: async handler deleted by the wrong thread</code>
This code example is taken from python <code>mmap</code> documentation, but in python 2.7 version everything works fine. Do you know when error could happen, I mean which line is wrong and why?


A:

It seems to be a bug.
Or maybe some feature.
The manual says:
<blockquote>
<p>Since the mmap() call opens and maps the object fd, all these operations on the file object f may interfere with the use of the memory map. This can be avoided by either working with an independent file descriptor, such as <code>&lt;code&gt;fd = os.open(filename, os.O_RDONLY)&lt;/code&gt;</code> and using <code>&lt;code&gt;mmap(fd)&lt;/code&gt;</code>, or by using the fileno() method on the file object f to get the file descriptor, <code>&lt;code&gt;fd =
