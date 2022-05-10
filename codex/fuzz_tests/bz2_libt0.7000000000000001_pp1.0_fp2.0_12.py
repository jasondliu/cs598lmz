import bz2
bz2.compress(b'felicia,tulips,tulips,tulips,tulips')

# 解压
f = bz2.BZ2File('file.bz2', 'wb')
f.write(b'hello world!')
f.close()

f = bz2.BZ2File('file.bz2', 'rb')
print(f.read())
f.close()

f = bz2.BZ2File('file.bz2', 'wb')
f.write(b'hello world!')
f.close()

f = bz2.BZ2File('file.bz2')
print(f.read())
f.close()
