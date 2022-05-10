import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Which gives <code>error: mmap can't extend file</code>. <code>m[:]</code> is empty but I would like to get the old content.
It is possible to get the content using <code>m.read(1)</code> but the question is is there an elegant way to do it using slices?


A:

You can use <code>mmap.move</code> to move the contents to the start of the <code>mmap</code> object.
<code>&gt;&gt;&gt; m = mmap.mmap(0, 10)
&gt;&gt;&gt; m[:] = b'hello'
&gt;&gt;&gt; m.tell()
0
&gt;&gt;&gt; m.seek(5)
5
&gt;&gt;&gt; m.write(b'world')
5
&gt;&gt;&gt; m[:]
b'helloworld'
&gt;&gt;&gt; m.tell()
10
&gt;&gt;&
