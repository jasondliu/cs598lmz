from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bzipped_file)

bzipped_file = bz2.BZ2File('input.py.bz2')
f = open('input.py', 'wb')
f.write(bzipped_file.read())

f.close()
