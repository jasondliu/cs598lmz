import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
On Windows, the last line raises <code>ValueError: mmap offset is greater than file size</code>, which is not a surprise since the file is truncated. On Linux, though, I see that <code>len(a) == 0</code> and I don't understand why.
Is it correct that the contents of the file are not removed when the file is truncated on Linux? If so, is there a way to tell mmap to re-read the file size?


A:

What you're seeing is by design.  When you <code>truncate</code> a file, the underlying file object doesn't change size immediately, so <code>mmap</code> doesn't change its size either.  The <code>mmap</code> is only updated when the file is closed, at which point it sees that the file has been truncated. (Files can be truncated via other methods too, such as <code>open(fn, O_TRUNC)</code>, so it's deliberate that <code>mmap</code> doesn't update when the file is truncated.)
In general you do not want <code
