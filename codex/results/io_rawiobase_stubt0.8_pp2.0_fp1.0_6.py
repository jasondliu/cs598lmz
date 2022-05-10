import io
class File(io.RawIOBase):
    def read(self,n=-1):
        return b'\x12\x34'
    def write(self,b):
        print(b)
File().read()

f=open('sample.txt','r')
print(f.read())
f.close()

f=open('sample.txt','r')
print(f.read())
f=open('sample.txt','r')
print(f.tell())
f.close()

f=open('sample.txt','rb')
print(f.read())
f.close()

f=open('sample.txt','rb')
print(f.read())
f.seek(0)
print(f.read())
f.close()

f=open('sample.txt','rb')
print(f.read(2))
f.seek(0)
print(f.read(2))
f.close()

f=open('sample.txt','rb')
for l in f:
    print(l,end='')
f.close()

f=open('sample.txt','
