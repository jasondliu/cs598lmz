import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The above code snippet is working fine. But when I replace the last two lines with following two lines, it is resulting in an error.
<code>    f.truncate()
    p = m.tell()
</code>
On executing this code I am getting following error message:
<code>Traceback (most recent call last):
  File "C:/Users/rajsr/PycharmProjects/ML/truncate.py", line 8, in &lt;module&gt;
    p = f.tell()
ValueError: File not open for reading
</code>
What is the reason for this issue?


A:

You are truncating the file. After truncating the file, your file object is no longer valid.
Quoting the docs for <code>mmap.mmap</code>
<blockquote>
<p>If the file changes on disk, the values in memory are not updated to match. In other words, this is by design not a “live view” of the underlying data.</p>
</blockquote>
The documentation for <code>mmap</
