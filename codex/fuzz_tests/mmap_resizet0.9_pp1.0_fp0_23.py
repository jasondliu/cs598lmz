import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Open the file in write binary mode, map the whole file, truncate it to zero bytes, and then try to read from the now nonexistent part of the file.
On Linux and OSX, this causes the process to terminate with a <code>SIGSEGV</code> error. On Windows and FreeBSD, the code runs to completion without an error.
I know it's somewhat counterintuitive to expect an error, since <code>truncate</code> can expand the file if needed, but I believe the issue is that the truncation happens after the memory is mapped, so there is no way to detect that the previous contents no longer exist. The third-party code I'm working with is using this behavior in order to implement a <code>StringIO</code>-like API on top of <code>mmap</code> (<code>getvalue</code>'ing the map, then <code>truncate</code>'ing it, then writing to it, then grow ing it and reading a small section of it... it's kind of complicated). This seems to work on Windows and FreeBSD, but I'm wondering if I can reliably detect this situation (on Linux and
