import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
returns an empty array (<code>bitarray</code> really). 
However if I do <code>f.truncate(1)</code>, I can get what I want.
I thought UNIX file system automatically truncates a file when the last part of it is written with an empty character. Is this false? How should I proceed?


A:

As the documentation of <code>mmap.mmap.read</code> states:
<blockquote>
<p><em>Note that if the <strong>mmap length is backed by file data</strong>, you cannot
  extend the underlying file and <strong>expect the <code>&lt;code&gt;mmap&lt;/code&gt;</code> to reflect the change</strong>.</em></p>
</blockquote>
(Emphasis mine.)
This means that if the <code>mmap</code> ended at the end of the file, you cannot reduce the size of the file by truncating it and then attempt to access the contents of the <code>mmap</
