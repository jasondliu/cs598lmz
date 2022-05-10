import lzma
lzma.HIGH_COMPRESSION
lzma.FORMAT_XZ

f = open('dmg-xcode.dmg', 'rb')
dmg = f.read()

f.close()

f = open('dmg-xcode-comp.dmg', 'wb')

f.write(lzma.compress(dmg, format=lzma.FORMAT_XZ))

f.close()

f = open('dmg-xcode-comp-xz.dmg', 'wb')

f.write(lzma.compress(dmg, format=lzma.FORMAT_XZ))

f.close()

f = open('dmg-xcode.dmg', 'rb')
data = f.read()
print('5.5.', data)
f.close()
print('5.5.1', data == lzma.compress(dmg))
print('5.5.2', data == lzma.compress(dmg, format=lzma.FORMAT_XZ))
