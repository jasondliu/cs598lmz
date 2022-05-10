import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The subprocess raises a <code>FileNotFoundError</code> exception due to the <code>mmap.mmap</code> method.
Is there a Python method that can map n bytes from <code>f.fileno()</code> in read-only mode?


A:

Remember that <code>mmap</code> works by creating a new file descriptor and mapping the file into your process's memory space.  This mapping does not persist across a <code>fork</code>.
The <code>fork</code> is performed when you call <code>subprocess.Popen</code>.  At that point, the child process is an exact copy of the parent process, and thus contains an exact copy of the <code>mmap</code> object.  It also has a new file descriptor opened from the same file as the parent, but this new file descriptor does not contain the <code>mmap</code> object or the mapped memory.  Note also that it does not contain the truncated file contents.
Since the child process doesn't have its own copy of the <code>mmap</code>,
