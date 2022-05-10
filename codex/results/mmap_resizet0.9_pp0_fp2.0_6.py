import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
After <code>f.truncate()</code> operation you'll get an exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
But <code>a = m[:]</code> expression should raise an exception because of index out of range.
Why am I getting an exception in the last string and not at <code>f.truncate()</code> time?


A:

The mmap spec says that if you try to mmap a region that is larger than the file size at the point the mmap is created, <code>mmap()</code> will fail completely and return <code>MAP_FAILED</code> indicating an error; one that your code did not check for:
<blockquote>
<p>Memory mapping a file is accomplished by calling mmap().  Unfortunately, <strong>this call is specific to certain OSs</strong> and must be handled through <code>&lt;code&gt;#ifdefs&lt;/code&gt;</code>. Some UNIX flavors that support mmap() will fail to map a file if
