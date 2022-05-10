import lzma
lzmaFile = lzma.LZMAFile('./test.xz')  # or fileobj=open("filename.xz", "rb")
file_content = lzmaFile.read()
print(file_content)

lzmaFile = lzma.LZMAFile('./test.xz', 'rb')
file_content = lzmaFile.read()
print(file_content)

lzmaFile = lzma.LZMAFile('./test.xz', 'r')
file_content = lzmaFile.read()
print(file_content)

lzmaFile = lzma.LZMAFile('./test.xz', 'r')
for line in lzmaFile:
    print(line)

import lzma

with lzma.LZMAFile('./test.xz', 'rb') as lzmaFile:
    for line in lzmaFile:
        print(line)

# compress
import lzma

with open('./test.txt',
