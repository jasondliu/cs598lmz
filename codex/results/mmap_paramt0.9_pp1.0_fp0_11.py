import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(9)
    print(m)
</code>
When I do so, I get the following error:
<code>m[0] = bytes(9)
TypeError: can't write bytes to text stream</code>
But I opened the file in binary mode.
The documentation says that the stream position should be <code>/dev/null</code>, but isn't it the case for me?
<blockquote>
<p>If fileno is not None, the mmap is initialized using the file specified by the fileno, the byte offset offset, and having the length size; fileno must be a valid (open) file descriptor. <strong>The file position is set to offset + length if offset &lt; 0; else, it is set to offset; if the file is opened in append mode, the file position will be set to the end of the file.</strong></p>
</blockquote>
My file is a binary file. What am I doing wrong?


A:

Based on your exception you have most likely opened the file in text-mode. The exception is raised by line 109 in
