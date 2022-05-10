import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

m.write(bytes(2))
print (m[:])
</code>
Using "wb" with r+b actually overwrites the file completely as well. You need to use "create" as the second parameter and indicate the file size. 

