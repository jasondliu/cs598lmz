import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints b'\x01', which is the expected behavior.
The code then breaks at this point, with the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: memoryview: slicing is not allowed on this type
</code>
I'm not sure why the error only occurs at the point where I slice the mmap.
I want to write the mmap to a file, and I want to do it by slicing the mmap, not by copying the mmap. This means I can't use os.write(m.fileno(),m[:]) because that would copy the whole mmap.
Can someone explain what is happening here?


A:

I have found a workaround.
This is the offending line:
<code>a = m[:]
</code>
This is the workaround:
<code>a = m[0:len(m)]
</code>
I am still not sure why this is happening, but the code seems to work
