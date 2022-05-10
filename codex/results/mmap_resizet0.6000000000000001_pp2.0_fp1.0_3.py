import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
The program prints <code>[1]</code> but I would expect it to raise an <code>OSError</code>. I am on Linux. Am I doing something wrong or is this a bug?
Update: I tested on Windows and the program raises an <code>OSError</code> as expected.

