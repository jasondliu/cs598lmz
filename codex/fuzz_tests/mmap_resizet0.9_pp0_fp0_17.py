import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
<blockquote>
<p>b''</p>
</blockquote>
There is a function called <code>resize</code> but it doesn't work on Windows.
What can I do to keep mmap synchronized with file?
P.S. My actual program reads lots of 8-byte records. I use functions like <code>mmap.find</code> and <code>mmap.index</code> to locate them. Therefore it is not possible to avoid using mmap for this kind of processing.


A:

On Windows, <code>resize</code> is broken, per the docs:
<blockquote>
<p>On Win32, <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code> will raise <code>&lt;code&gt;EnvironmentError&lt;/code&gt;</code> if the file size is
      changed after the <code>&lt;code&gt;mmap()&lt;/code&gt;</code> was created. None of the other mm
