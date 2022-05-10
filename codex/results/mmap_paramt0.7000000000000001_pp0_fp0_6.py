import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
</code>
The above code works. I can read the byte and print out the byte value. However, if I want to write to the file and read it again, it doesn't work.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.seek(0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
The above code reads the byte, writes another byte and then reads again. When it tries to print the byte again, I get the following error.
<code>Traceback (most recent call last):
  File "a.py", line 12, in &lt;module&gt;
    print(m.read(1))
ValueError: read of closed file
</code>
How do I read
