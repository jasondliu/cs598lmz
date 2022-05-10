import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
gives
<code>b''
</code>
as output. Shouldn't a have been b'1'? The file gets completely truncated. If I comment out the <code>f.truncate()</code> line, then the output is b'1', as one would expect. I would like to truncate the file and continue reading it, for example with numpy. I already have the workaround <code>m.close()</code> and <code>m = mmap.mmap(f.fileno(), size)</code> after opening the file again and setting size equal to the new file size, but I would like to know what is going on.


A:

From the doc:
<blockquote>
<p>All methods except readinto() and resize() raise ValueError on
  error.</p>
</blockquote>
So I'm assuming you get an error. What happens if you catch it and print it?
Also, what happens if you use:
<code>with open('test', 'r+b') as f:
    print("mmap")
    m
