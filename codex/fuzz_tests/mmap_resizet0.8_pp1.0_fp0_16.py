import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When I run the program and check the content of test file, it's empty. Why? Shouldn't it preserve the content of the file?


A:

As requested, I'll quote relevant parts of the documentation and then attempt to explain.
<blockquote>
<p>POSIX requires that a read() which can be proved to occur after a write() returns the new data. Similarly, a write() which can be proved to occur after another write() to the same location is required to be atomic. These are <strong>guaranteed only for normal files</strong> and <strong>for block devices</strong> (such as the Linux <em>/dev/hda</em> device node) which have a block size equal to the filesystem block size.</p>
</blockquote>
(Emphasis mine)
So, in Python, this is documented, for the <code>os.write</code> function, as:
<blockquote>
<p>On Unix, if <em>fd</em> is a regular file, this method <strong>writes the bytes but does not change the file offset</strong> (it does not
