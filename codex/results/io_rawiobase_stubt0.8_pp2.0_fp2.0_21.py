import io
class File(io.RawIOBase):
    def close(self):
        os.close(self.handle)

f = open('name.txt')
f.read(2)
f.read()
f.read(1)
f.close()
f.read()
with open('name.txt') as f:
    print(f.read())
import os
os.close(f.fileno())
import io
f = io.open('file.txt', 'r', encoding='mbcs')
f.read()
f.close()
f.read()
f = io.open('file.txt', 'r', encoding='utf-8')
f.read()
f.close()
f = io.open('file.txt', 'r', encoding='utf-8')
f.read()
f.readline()
f.readline()
f.readlines()
f.seek(0)
f.readlines()
f.seek(0)
f.readlines()
f.seek(0)
f.readlines()
f.seek(0)
f.readlines()
f.close()

