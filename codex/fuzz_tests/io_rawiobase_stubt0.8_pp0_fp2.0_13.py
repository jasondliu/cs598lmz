import io
class File(io.RawIOBase):
    def __init__(self,file):
        self.file = file
    def read(self,size=-1):
        return self.file.read(size)
    def write(self,b):
        self.file.write(b)
    def close(self):
        pass

#######

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

s = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = s.readline()
    if s == '':
        break
    print(s.strip())


from io import BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())
