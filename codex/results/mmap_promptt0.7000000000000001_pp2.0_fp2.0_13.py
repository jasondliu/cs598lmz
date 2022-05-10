import mmap
# Test mmap.mmap

with open("test.txt", "w") as f:
    f.write("hello world!")

with open("test.txt", "r") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
    m.seek(0)
    print(m[6:10])
    m.close()

import os

print(os.system("ls"))
print(os.system("pwd"))

# Print to file
with open('test2.txt', 'w') as f:
    f.write('hello world!\n')
    f.flush()
    f.write('hello world!\n')
