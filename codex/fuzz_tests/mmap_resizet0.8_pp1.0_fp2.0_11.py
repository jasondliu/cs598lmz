import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
The above code is running on Python 3.6 and Python 3.7 as well. The output is as follows:
<code>b'\x01'
</code>
The <code>f.truncate()</code> function truncates the file to size 0 and hence the content is lost. But the memory map is still getting the data <code>b'\x01'</code>. This is not the expected behavior because if the content of file changes then the mmap should also change accordingly.
My question is, is this expected behavior or is triggered by some bug?
I found a similar question in the past but it did not answer my question.

