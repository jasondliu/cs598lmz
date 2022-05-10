import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
If I don't use <code>mmap</code> and just read from the file, I can read the data. Is this expected behavior?


A:

Yes, this is expected behavior. <code>mmap</code> doesn't work with files that are truncated.
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map will be the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called. <strong>Files can be truncated</strong> either by using <code>&lt;code&gt;os.ftruncate()&lt;/code&gt;</code> on an open file descriptor, or by setting the file size using <code>&lt;code&gt;os
