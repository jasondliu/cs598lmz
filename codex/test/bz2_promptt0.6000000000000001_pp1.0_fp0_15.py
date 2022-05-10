import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    f = bz2.open('bz2_file.txt', 'wb')
except IOError:
    print("File not found or path is incorrect")

f.write(b'This is a test')
f.close()

f = bz2.open('bz2_file.txt', 'rb')
