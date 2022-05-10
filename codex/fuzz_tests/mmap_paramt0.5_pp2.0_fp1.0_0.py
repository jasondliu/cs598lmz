import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    print(m[0] == 1)
</code>
And I got:
<code>1
False
</code>
The question is why the <code>m[0]</code> is not equal to <code>1</code>?
I think the <code>m[0]</code> should be <code>1</code>.


A:

<code>bytes</code> objects are immutable, so you can't change the value of one.
<code>&gt;&gt;&gt; b = bytes(1)
&gt;&gt;&gt; b[0] = 1
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'bytes' object does not support item assignment
</code>
So, <code>bytes(1)</code> returns a <code>bytes</code> object of length 1, with the first byte set to 0.
If you want to create a <code>bytes</code> object with a
