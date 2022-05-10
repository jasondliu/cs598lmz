import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
</code>
It seems that this could be the answer, but I don't know if there is a way of converting the data to the new file size, or if there is a better way of doing this.


A:

You can't truncate a file that is mmap'ed at the moment. From the docs:
<blockquote>
<p>For methods which change the size of the object, note that close can
  be called before all the data is written and that flush is not
  called at all.</p>
</blockquote>
Truncate is one of the methods that changes the size of the object.

