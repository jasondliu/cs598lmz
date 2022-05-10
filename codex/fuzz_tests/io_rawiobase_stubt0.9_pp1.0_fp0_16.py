import io
class File(io.RawIOBase):
    def write(self, b):
        print(b)

f = File()
f.write(b'hello \n')

with open('sample.txt', 'w') as f:
    f.write('hello')
    f.write('world')

with open('sample.txt', 'r') as f:
    read_data = f.read()

print(read_data)

#%%
import mmap
buf = mmap.mmap(-1, 1000, access=mmap.ACCESS_READ)
print(buf[:10])
buf.close()

#%%
import os
print(os.environ)
for name in ['HTTP_USER_AGENT', 'HOME', 'PATH']:
    if name in os.environ:
        print('%s = %s' % (name, os.environ[name]))


#%%
