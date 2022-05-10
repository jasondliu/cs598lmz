import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48

with open('test2', 'wb') as f:
    f.write(bytes(1))

with open('test2', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 49
    m.close()


import os

print(os.listdir('.'))
os.rename('test', 'testnew')
print(os.listdir('.'))
os.rename('testnew', 'test')
print(os.listdir('.'))

import os

print(os.listdir('.'))
os.system('mv testtest2 test2test')
print(os.listdir('.'))
os.system('mv test2test testtest2')
print(os.listdir('.'))


import os

with open('test', 'wb') as f:
    f.write(bytes(10))
with open('test2', 'wb') as f:
    f.write(bytes(10))

print
