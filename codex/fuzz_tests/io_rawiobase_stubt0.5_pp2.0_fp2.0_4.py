import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def read(self, n):
        with open(self.file_name, self.mode) as f:
            return f.read(n)

f = File('foo.txt', 'r')
f.read(5)

#readlines()
f = open('foo.txt', 'r')
f.readlines()
f.close()

#write()
f = open('foo.txt', 'w')
f.write('Python is fun!')
f.close()

#writelines()
f = open('foo.txt', 'w')
f.writelines(['Python\n', 'is\n', 'fun!\n'])
f.close()

#seek()
f = open('foo.txt', 'r')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)

#tell()
f = open('foo.txt
