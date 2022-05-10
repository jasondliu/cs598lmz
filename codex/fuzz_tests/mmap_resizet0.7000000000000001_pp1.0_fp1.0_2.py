import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When I run this, I get the following exception:
<code>Traceback (most recent call last):
  File "C:\Users\Nicolas\Desktop\test.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
I thought that if <code>mmap</code> is set to 0, it will resize itself to the size of the file. Why doesn't it work?
(I can't use the <code>mmap.resize()</code> method, because it is not available on Windows.)


A:

The solution is to open the file in <code>r+b</code> mode instead of <code>r</code>. This is because <code>r+</code> mode opens the file in read-write mode and the <code>+</code> sign is only added to the <code>r</code> mode to indicate that you can also write to the <code>mmap</code>.
<code>import mmap

with open('
