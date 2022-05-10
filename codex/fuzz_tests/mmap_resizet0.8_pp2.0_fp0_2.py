import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the <code>f.truncate()</code> to throw a <code>mmap.error: cannot resize a mapped file</code> exception.
But it doesn't.

File is not <code>m.PAGESIZE</code> aligned.
Executed on Python 3.6 on Windows 10.
Am I doing something wrong or is this a bug?


A:

As you mentioned, <code>truncate</code> throws the exception when called from an mmap object, but does not throw the exception when called from a file handle.  This is because the <code>truncate</code> method is implemented on the file object and not the mmap object.  If you call the <code>truncate</code> method on the file object, it will throw the expected exception.
Since the problem is triggered by calling <code>truncate</code> on the file object, this is possibly a bug.  If so, it is probably a bug in the <code>truncate</code> method of the file object.
When called from a file handle, the <code>truncate
