import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = ord('a')
    m.flush()
</code>
This code works. But I wonder, what is the difference between using <code>wb</code> and <code>r+b</code> in <code>with open('test', 'wb') as f</code>?


A:

The <code>b</code> at the end of both file modes is a binary mode flag.  You can leave it off or use <code>t</code> instead, but if you do, you'll need to decode and encode the bytes going into and out of the file.  Using the <code>b</code> flag makes all the data read and written raw.  See the Python file modes documentation.
The <code>r</code> in <code>r+b</code> means open the file for reading and writing.  The <code>+</code> is not required.  You can use it with the <code>w</code> flag to open a file for reading and writing.  
The <code>w</code> in <code
