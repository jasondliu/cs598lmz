import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
This code fails with <code>ValueError: mmap can't modify a readonly memory map</code> on Windows but works on Linux.
Is there a way to make it work on Windows?


A:

The documentation for <code>mmap</code> states:
<blockquote>
<p>On Windows, the file handle <em>fid</em> must be opened with <code>&lt;code&gt;CreateFile&lt;/code&gt;</code> using the <code>&lt;code&gt;FILE_MAP_WRITE&lt;/code&gt;</code> flag, and the <em>access</em> argument must specify <code>&lt;code&gt;ACCESS_WRITE&lt;/code&gt;</code>.</p>
</blockquote>
The <code>CreateFile</code> documentation shows that <code>FILE_MAP_WRITE</code> is a combination of <code>GENERIC_WRITE</code> and <code>FILE_
