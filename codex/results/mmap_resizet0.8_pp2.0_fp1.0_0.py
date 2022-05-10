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
After running this code, I expect a to contain [0] since the file was truncated and should contain only the null byte (and the following read should give EOF). However, a is [1] as if the file was not truncated. 
I am not sure if the behavior is wrong or not, but I would like to know if there is a way to flush the mmap object, like I do with m.flush(), but for the content read.

