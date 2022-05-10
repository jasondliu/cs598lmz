import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(8))
 
with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m[8])
</code>
The output is:
<code>b'\x00'
</code>
The mmap module's documentation states:
<blockquote>
<p>If you want to map an existing Python file object, use its <code>&lt;code&gt;fileno()&lt;/code&gt;</code>
  method to obtain the correct value for the <code>&lt;code&gt;fileno&lt;/code&gt;</code> parameter.</p>
</blockquote>
I am not sure what the <code>fileno()</code> method is returning and why it is correct. I think it is returning the file object's file descriptor, which I think should result in <code>mmap.mmap()</code> throwing an exception about the file descriptor not being a valid file.
I am using python 3.
