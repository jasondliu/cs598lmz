import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
#output: IndexError: mmap index out of bounds
</code>
As specified in the doc, the <code>mmap.mmap.read</code> method is equivalent to <code>mmap.mmap.__getitem__</code> in the above code, but effectively, <code>__getitem__</code> doesn't raise exception while <code>read</code> does.
What is the difference between <code>__getitem__</code> and <code>read</code> in terms of mmap?
My question is not the same as this one. In the above code, a new <code>mmap.mmap</code> object is created and it's length is not changed, only the file beneath has been changed.


A:

<blockquote>
<p>What is the difference between <code>&lt;code&gt;__getitem__&lt;/code&gt;</code> and <code>&lt;code&gt;read&lt;/code&gt;</code> in terms of mmap?</p>
</blockquote>
So, the <code>
