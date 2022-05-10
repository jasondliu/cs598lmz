import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And I'm getting a <code>mmap.error: cannot enlarge memory arrays</code> in the last line? What am I doing wrong?


A:

The problem is that you are modifying the <code>mmap</code> object while you are trying to access it.
When you truncate the file, the <code>mmap</code> object is pointing to a part of the file that no longer exists.
The fix is to do the read before you truncate the file.

