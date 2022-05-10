import bz2
# Test BZ2Decompressor.
with open("C:\\Users\\IT\\Downloads\\test.bz2", "rb") as input:
    with bz2.BZ2File("C:\\Users\\IT\\Downloads\\test.txt", "w") as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(data)
import shutil
with open("C:\\Users\\IT\\Downloads\\test.bz2", "rb") as input:
    with bz2.open("C:\\Users\\IT\\Downloads\\test.txt", "wt") as output:
        shutil.copyfileobj(input, output)

import gzip
# Test GzipFile.
with gzip.open("C:\\Users\\IT\\Downloads\\test.gz", "wb") as output:
    output.write(b"hello world!")
with gzip.open("C:\\Users\\IT\\Downloads\\test.gz", "rt") as input:
    print(input.read())
print()
# Test GzipFile with filename
