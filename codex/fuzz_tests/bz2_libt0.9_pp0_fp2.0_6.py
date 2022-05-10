import bz2
bz2_file = bz2.BZ2File("sample.bz2")
data = bz2_file.read()
bz2_file.close()
print(data)

# gzip
import gzip
gzip_file = gzip.open("sample.txt.gz", "rb")
data = gzip_file.read()
gzip_file.close()
print(data)
