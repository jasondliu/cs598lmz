import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

print(m)

# close the file and open a new one.
m.flush()
m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

print(m)
</code>
The last print actually prints a valid mmap object and can be used to read and write memory as expected. 
But is there a better way to do this?
Thanks,
Dan


A:

You can use file.truncate() to change the file size.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate(0)
    m = mmap.mmap(f.fileno(), 0)

print(m)
</code>

