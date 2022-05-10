import bz2
bz2File = bz2.BZ2File('sample.bz2')
print(bz2File.read())
bz2File.close()
