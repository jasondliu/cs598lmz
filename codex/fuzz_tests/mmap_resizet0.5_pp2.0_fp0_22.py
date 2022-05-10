import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
So what I expect is that the <code>m</code> map is updated when <code>f.truncate()</code> is called, but I get a <code>ValueError: mmap length is zero</code> exception.
Is there any way to update the <code>mmap</code> object when the file is truncated?


A:

The documentation for <code>mmap</code> states:
<blockquote>
<p>The data in a <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is normally cached in memory, but <strong>can also be written to disk if needed</strong>. <strong>The data in a <code>&lt;code&gt;mmap&lt;/code&gt;</code> object can be accessed and modified like a string</strong>, but if you modify it, the changes are <strong>written back to the original file</strong>.</p>
</blockquote>
So, to truncate the file, you need to do this:
<code>m
