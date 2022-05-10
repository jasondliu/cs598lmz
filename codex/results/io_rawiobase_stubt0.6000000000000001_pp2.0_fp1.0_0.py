import io
class File(io.RawIOBase):
    def read(self, n=-1):
        print('read', self, n)
        return super().read(n)

    def write(self, b):
        print('write', self, b)
        return super().write(b)
f = File()
f.read()
f.write(b'xxx')

import sys
sys.stdout = File()
print('spam')

class SubFile(File):
    def read(self):
        print('sub read')

f = SubFile()
f.read()

f = File()
f.read()

class SubFile(File):
    def read(self):
        print('sub read')
        return super().read()

f = SubFile()
f.read()

class SubFile(File):
    def read(self):
        print('sub read')
        return super().read(10)

f = SubFile()
f.read()

class SubFile(File):
    def read(self):
        print('sub read')
        return super().read(10)


