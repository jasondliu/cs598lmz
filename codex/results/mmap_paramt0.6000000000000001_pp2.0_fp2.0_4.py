import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'x'
    print(m[0])

with open('test', 'rb') as f:
    print(f.read())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'x'
    print(m[0])

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is:
<code>$ python3 test.py 
120
b'x'
120
b'x'
</code>
So, I am able to change the content of the file using <code>mmap</code>.
However, when I do the same thing with a file opened in append mode (<code>'ab'</code> or <code>'ab+'</code>), I get the following:
<code>$ python3 test.py 
Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
