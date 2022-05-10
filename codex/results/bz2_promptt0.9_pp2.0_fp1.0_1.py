import bz2
# Test BZ2Decompressor
bz2dc = bz2.BZ2Decompressor()
try:    
    with open(path.join(fpath,'panda.csv.bz2'),'rb') as f:
        for td in iter(lambda: f.read(256*1024), b''):
            data = bz2dc.decompress(td)
            if data:
                sys.stdout.buffer.write(data)
                sys.stdout.flush()
except IOError:
    pass

print(data)

# Test BZ2File
bz2f = bz2.BZ2File(path.join(fpath,'panda.csv.bz2'))
print(bz2f.read())

lzmaf = lzma.LZMAFile(path.join(fpath,'panda.csv.xz'),mode='rb')
print(lzmaf.read())
lzmaf.close()

myf = bz2.open(path.join(fpath,'panda.csv.bz2'),'rt
