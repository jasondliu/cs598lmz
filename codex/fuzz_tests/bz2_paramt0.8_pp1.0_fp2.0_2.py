from bz2 import BZ2Decompressor
BZ2Decompressor(open("dump.rdb","rb"))

fout = open("dump.rdb","wb")

with open("dump.rdb.bz2", "rb") as f:
    decompressor = BZ2Decompressor()
    for block in iter(lambda : f.read(100 * 1024), b''):
        fout.write(decompressor.decompress(block))
    
    decompressor.flush()
    fout.write(decompressor.decompress(decompressor.unused_data))

fout.close()

#restore 
redis-cli -h ip -p port  -a password
