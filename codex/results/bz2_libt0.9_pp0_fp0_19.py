import bz2
bz2.decompress(bz2.BZ2File('bz2File.bz2').read())

import gzip as gz
gz.GzipFile('gzipFile.gz').read()
#To compress (or decompress) binary data
import bz2
data = bz2.compress(b'My compressed text')
data
bz2.decompress(data)

#To compress the file, you can use bz2.compress() instead. For larger files, this approach is safer.
with open('uncompressedFile.txt', 'rt') as rf:
    data = rf.read()
data[:50]

with bz2.BZ2File('bz2File.bz2', 'wt') as wf:
    wf.write(data)
with bz2.BZ2File('bz2File.bz2', 'rt') as rf:
    print(rf.read()[:50])
# The output is the same as the original text.


#The same approach can be applied to gz
