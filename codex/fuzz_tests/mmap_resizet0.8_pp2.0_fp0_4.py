import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is '\x01'.  This is a buffer for data written before the truncate, so I guess this is caching.  Although <code>m[0]</code> is <code>1</code>, <code>m[:] == ''</code>.
I would like to use such a buffer in order to get around a file race problem.  I want to write, then truncate and read the result.  Writing, truncating, and reading fails because of a race condition.  Reading, then truncating and writing also fails because of a race condition.  If a buffer exists between write and truncate, then I can avoid the race condition by truncating, writing then reading.  However, I only see this behaviour when using <code>mmap</code>.  I have tried manually using <code>lseek</code>, but I can't get the same behaviour to occur.
Is mmap caching a documented feature?  Is there another way to make this cache without using <code>mmap</code>?


A:

The answer is <code>fsync</code>.  You are actually not reading cached data
