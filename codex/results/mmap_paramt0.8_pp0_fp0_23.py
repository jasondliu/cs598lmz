import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'3'

os.remove('test')
</code>
I wonder why it doesn't raise a <code>ValueError</code> for writing <code>bytes(1)</code> which is just a single <code>bytes</code> object with length 1 into a <code>bytes</code> object. From the docs it says
<blockquote>
<p>encoding and errors must not be provided</p>
</blockquote>
and it is obvious that <code>bytes(1)</code> is not a valid encoding.
Am I missing something?


A:

It's your code that fails to adhere to the specification.
From the <code>bytes()</code> constructor documentation:
<blockquote>
<p>The <code>&lt;code&gt;bytes()&lt;/code&gt;</code> constructor returns a bytes object. It optionally accepts an encoding and errors keyword argument, for example: <code>&lt;code&gt;bytes('abc', 'utf-8')&lt;/code&gt;</code></p>
<p
