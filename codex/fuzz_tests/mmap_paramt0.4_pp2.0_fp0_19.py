import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    m.write(bytes(10))
    m.seek(0)
    print(m.read(10))
    m.close()
</code>
This works fine on Linux, but on Windows it gives an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(10)
OSError: [WinError 87] The parameter is incorrect
</code>
I'm using Python 3.6.1 32-bit on Windows 7 64-bit.
Is there some way to get this to work on Windows?


A:

The problem is that the file was opened in text mode, and <code>mmap</code> doesn't support text mode.
The solution is to open the file in binary mode. This can be done by adding <code>b</code> to the mode:
<code>with open('test', 'r+b') as f:
</code>

