import io
class File(io.RawIOBase):
    def readable(self):
        return True
class File1(io.TextIOBase):
    def readable(self):
        return True

f=File()
print(f.readable())
f1=File1()
print(f1.readable())

# Byte-stream classes
# RawIOBase
# BufferedIOBase
# TextIOBase

# FileIO
# BufferedReader
# BufferedWriter
# BufferedRandom
# BufferedRWPair
# TextIOWrapper
# StringIO
# BytesIO

f=open('numbers.txt','r')
for line in f:
    print(line,end="")
f.close()

f=open('d:/abc.txt','w')
f.write('sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfs
