import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.close()
    print(a)
</code>
This prints <code>b''</code>, but I expect it to throw an exception.
The same happens with Python 3.4.3, but it works as expected with Python 2.7.10.
Is this a bug in Python 3 or expected behaviour?


A:

<blockquote>
<p>Is this a bug in Python 3 or expected behaviour?</p>
</blockquote>
It is expected behaviour. The Python 3 <code>mmap</code> documentation states:
<blockquote>
<p>The module defines the following exceptions:</p>
<p><code>&lt;code&gt;exception mmap.error&lt;/code&gt;</code></p>
<p>This exception is raised on any error. It is a subclass of <code>&lt;code&gt;OSError&lt;/code&gt;</code>.</p>
</blockquote>
The Python 2 <code>mmap</code> documentation has the same section, but the exception type is <code>mmap.error</
