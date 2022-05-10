import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.close()
</code>
Seeing what I want to do here, maybe I should open b'r+' and do <code>m.seek()</code> instead of a slice?


A:

You cannot mix mmap with writes to the file while the mmap is active, see Python mmap documentation.
You can either write to the file separately:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    f.close()
    a = m[:]
</code>
or try something like:
<code>m.resize(0)
m.close()
a = open('test').read()
</code>
<blockquote>
<p>maybe I should open b'r+' and do <code>&lt;code&gt;m.seek()&lt;/code&gt;</code> instead of a slice?</p>
</blockquote>
You can use <code>m.seek()</code> instead of a slice to set
