import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/mike/PycharmProjects/test/test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can see that the error is correct, but I don't understand why. How can the offset be greater than the file size when it's always 0?


A:

The issue is that you are opening the file in <code>r+b</code> mode, which allows you to both read and write to the file.
However, once you have truncated the file, there is no longer anything to read.
If you open the file in <code>r+b</code> mode, and then truncate it, there is no longer anything to read. 
This is not the same as opening the file in <code>wb</code> mode, which only allows writes. 
In the latter case, the truncation is performed before the data is written. In the former case, the truncation
