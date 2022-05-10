import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('wiki.xml.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100 * 1024), b''):
        try:
            unzipped = decompressor.decompress(block)
            print(unzipped)
        except Exception as e:
            pass

######################################################################
     
import gzip

# Test GzipFile
with gzip.open('wiki.xml.gz') as f:
    print(f.read())
