import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(1))
    m.write_byte(bytes(2))
    m.write_byte(bytes(3))
    m.write_byte(bytes(4))
    m.flush()

with open('test', 'rb') as f:
    print("File content:", file.read(f))
</code>
When running this, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    m.write_byte(bytes(1))
ValueError: byte must be in range(0, 256)
</code>
If I change the byte to 0, it works just fine.
What byte value do I need to pass to write_byte to write it to the file?


A:

You're creating a one-element byte array with value 1 when you do <code>bytes(1)</code>.
To write a single byte you need to pass an integer to <code>write_byte</code>:
<code>m.write_byte(
