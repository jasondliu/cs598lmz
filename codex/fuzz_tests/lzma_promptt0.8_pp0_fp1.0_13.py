import lzma
# Test LZMADecompressor

with lzma.open('../../Book.scnassets/Book/xz/document.json.xz') as xz_file:
    with open('document.json', 'wb') as raw_file:
        with lzma.LZMADecompressor() as decompressor:
            while True:
                chunk = xz_file.read(1024)
                if not chunk:
                    break
                raw_file.write(decompressor.decompress(chunk))
 
import gzip
# Test GzipFile

with gzip.open('../../Book.scnassets/Book/gz/document.json.gz') as gz_file:
    with open('document.json', 'wb') as raw_file:
        while True:
            chunk = gz_file.read(1024)
            if not chunk:
                break
            raw_file.write(chunk)
 
import bz2
# Test BZ2File

with bz2.open('../../Book.scnassets/Book/bz2/document.json
