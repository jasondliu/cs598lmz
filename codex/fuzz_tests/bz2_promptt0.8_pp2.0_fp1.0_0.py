import bz2
# Test BZ2Decompressor
data = open("./data/sample.bz2", 'rb').read()

for i in range(1, 10):
    d = bz2.BZ2Decompressor()
    t0 = time.time()
    u = d.decompress(data[:i*100000])
    print(i, len(u), time.time() - t0)

t0 = time.time()
d = bz2.BZ2Decompressor()
u = d.decompress(data)
print("Total:", len(u), time.time() - t0)

u == open("./data/sample.txt", 'rb').read()

# The followin code will fail as the BZ2Decompressor can only deal with bz2 files
#open('/usr/share/doc/python/copyright.gz', 'rb').read() 
#d = bz2.BZ2Decompressor()
#u = d.decompress(data)
#u == open('/usr/share/doc/python/copyright',
