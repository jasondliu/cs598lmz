import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # Crash here.
</code>
I've just found that this only causes a crash on Linux. On Windows, <code>a</code> contains nothing as expected.
Is this a bug in <code>mmap</code> or <code>truncate</code>? Or is this actually documented behaviour somewhere?


A:

This is a long-standing bug in Python's <code>mmap</code> library: http://bugs.python.org/issue17908
It is also a bug in the C library - <code>munmap</code> should set errno to <code>EINVAL</code> but it doesn't (e.g. glibc's bugreport for it:  https://sourceware.org/bugzilla/show_bug.cgi?id=12392).
That said, the <code>m[:]</code> doesn't require a memory read, since it is a byte-slice of everything, so <code>m[:1]</code> would be a read from before the crash and <code>m[2:]</code> would crash.

