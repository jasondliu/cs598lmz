import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError</code>:
<code>ValueError: mmap offset is greater than file size
</code>
I would have expected the <code>mmap</code> object to be updated to the new file size. Is this a bug, or is there a way to make it work?


A:

<code>mmap</code> is implemented in C, and uses the <code>lseek()</code> function to get the size of the file. <code>lseek()</code> is documented as:
<blockquote>
<p>lseek() sets the file offset for the open file
         descriptor fd to the argument offset according to the directive
         whence as follows:</p>
<pre><code>&lt;code&gt;   SEEK_SET The file offset is set to offset bytes.

   SEEK_CUR The file offset is set to its current location plus offset
            bytes.

   SEEK_END The file offset is set to the size of the file plus offset
            bytes.
&lt;/code&gt;</code></pre
