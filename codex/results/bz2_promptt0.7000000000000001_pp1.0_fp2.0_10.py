import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        
        output.write(decompressor.flush())

!cat data/sample.out

!rm data/sample.out
import bz2
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    print(input.read())
 
import bz2

with bz2.open('data/sample.bz2', 'rt') as input:
    print(input.read())
 
import bz2

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    print(input.readline())
   
