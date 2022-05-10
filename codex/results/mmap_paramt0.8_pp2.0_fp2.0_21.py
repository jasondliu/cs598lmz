import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0, os.SEEK_END)
    m.write(b'abc')
    m.write(b'def')

print(*open('test', 'rb'))
</code>
The output is <code>1</code> (as opposed to the expected <code>1abcdef</code>).
I have tried various combinations of <code>mmap</code>'s <code>ACCESS_*</code> constants, <code>os</code>'s <code>SEEK_*</code> constants, and <code>open</code>'s <code>mode</code> string arguments <code>r+b</code> <code>r</code> <code>w</code> <code>w+</code> <code>r+</code> <code>rb+</code> <code>w+b</code> with no success.
What is the correct way to open a file for appending in Python?
EDIT: I am using Python 2.7 on Windows 7


A:

<code>os.SEEK_END</code>
