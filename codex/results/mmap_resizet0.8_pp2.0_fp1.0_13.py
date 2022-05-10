import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
The error I get is:
<code>Traceback (most recent call last):
  File "/Users/username/Desktop/test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>


A:

I can't reproduce your problem, but I can give you a working snippet.
The main problem is probably in your understanding of the mmap length.
In your code, the length is specified as 0, which is a valid value (according to the python doc):
<blockquote>
<p><strong>length</strong> : Optional</p>
<p>Number of bytes to map. If length is omitted, the map extends to the end of the file. </p>
</blockquote>
So you create a 0-length mmap (which is still valid, but very short and useless).
Then, you truncate your file (which effectively resets the length of your file to 0 bytes). 
And finally, you're trying to read a slice of your mmap,
