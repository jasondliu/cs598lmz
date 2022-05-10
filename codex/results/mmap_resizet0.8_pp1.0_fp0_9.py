import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code has two different behaviors: on machine A, running Python 3.5.2, <code>mmap</code> raises a <code>ValueError</code> (which is expected). On machine B, running Python 3.6.3, it is completely silent (which is not expected).
A similar behavior is observed when <code>truncate</code> is replaced by <code>ftruncate</code>, or when the size of the file is larger.


A:

It turns out you have found a bug in the <code>mmap</code> module! The behavior is different depending on if you are using the posix or windows versions, and it looks like the posix version is more conservative and catches the error:
Here's the posix version:
<code>/*  Fetch the page of memory containing the requested byte.  */

if (flags &amp; MAP_PRIVATE) {
    if (pos + size &gt; filesize) {
        errno = EINVAL;
        return MAP_FAILED;
    }
    return mmap(NULL, size, PROT_
