import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect the output to be <code>b'\x00'</code> but the actual output is <code>b'\x01'</code>.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

The documentation says:
<blockquote>
<p>The optional <em>length</em> argument specifies the <strong>maximum</strong> size of the
  mapped region. If <em>length</em> is larger than the current size of the file,
  the file is extended to contain <em>length</em> bytes. If <em>length</em> is omitted,
  the maximum size of the mapped region is the current size of the file,
  as reported by the <code>&lt;code&gt;os.path.getsize()&lt;/code&gt;</code> function.</p>
</blockquote>
So, when you truncate the file, the mapping is still valid, but it is not updated.

