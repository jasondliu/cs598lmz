import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b''
    def write(self, b):
        return len(b)
f = File()
print(f.write(b'Hello'))
print(f.read(4))
print(f.read())

# io.StringIO
# io.StringIO是一个在内存中读写str的类，与io.BytesIO类似
f = io.StringIO()
print(f.write('Hello'))

f = io.StringIO('Hello\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# io.BytesIO
# io.BytesIO是在内存中操作bytes的方法，使得和读写文件具有一致的接口
f = io.BytesIO()
f.write(b'
