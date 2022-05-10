import bz2
# Test BZ2Decompressor
with open('sample.bz2', 'rb') as fin:
    with bz2.BZ2Decompressor() as dec:
        with open('sample.txt', 'wb') as fout:
            while True:
                block = fin.read(1024)
                if not block:
                    break
                fout.write(dec.decompress(block))
# Test BZ2File
with bz2.BZ2File('sample.bz2', 'rb') as fin:
    with open('sample2.txt', 'wb') as fout:
        for line in fin:
            fout.write(line)
 
# Test BZ2Compressor
with open('sample.txt', 'rb') as fin:
    with bz2.BZ2Compressor() as comp:
        with open('sample2.bz2', 'wb') as fout:
            while True:
                block = fin.read(1024)
                if not block:
                    break
                fout.write(comp.compress(block))
            fout.write(comp
