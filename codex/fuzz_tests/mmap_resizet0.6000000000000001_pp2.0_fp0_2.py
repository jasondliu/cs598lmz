import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    f.close()
    print(a)
</code>
This gives me: <code>IndexError: cannot fit 'mmap' object into an index-sized integer</code>
I'm using Python 3.6.3.


A:

You are trying to access <code>m</code> after <code>truncate</code>ing the file.
The documentation says:
<blockquote>
<p>If length is larger than the current size of the file, the file is extended with <code>&lt;code&gt;NUL&lt;/code&gt;</code> bytes. The file’s current position isn’t changed.</p>
</blockquote>
If you remove the <code>truncate</code> call, you will see that it works just fine.

