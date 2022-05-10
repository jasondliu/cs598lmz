import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[1] = bytes(2)
</code>
The output is:
<code>&gt;&gt;&gt; 
&lt;mmap.mmap object at 0x000000000262D9E8&gt;
Traceback (most recent call last):
  File "C:\mmap_tester.py", line 10, in &lt;module&gt;
    m[1] = bytes(2)
ValueError: cannot modify size of mapped region
&gt;&gt;&gt; 
</code>

