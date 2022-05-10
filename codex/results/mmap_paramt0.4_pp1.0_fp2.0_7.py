import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
The file is updated with the byte '2' as expected.
However, when I do the same thing with a file that is located on a remote share, I get the following exception:
<code>Traceback (most recent call last):
  File "C:/Users/user/PycharmProjects/test/test.py", line 9, in &lt;module&gt;
    m.write(bytes(2))
OSError: [WinError 87] The parameter is incorrect
</code>
The file is not updated.
I am using Python 3.6.1 and Windows 7.

