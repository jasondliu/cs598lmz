import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected this to give a <code>ValueError</code>: <code>mmap slice length is zero</code>. Why does this work?


A:

This is a trick question.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
is equivalent to:
<code>m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, 0, 0)
</code>
The default value of <code>mmap.MAP_SHARED</code> is <code>0</code>, which is a synonym for <code>mmap.MAP_PRIVATE</code>. You can fix this by using <code>mmap.MAP_SHARED</code> explicitly:
<code>m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED)
</code>
The reason it works in your case is because, according to the docs (emphasis mine):
<blockquote>
<p>The <code>&lt;code&gt;length&lt;
