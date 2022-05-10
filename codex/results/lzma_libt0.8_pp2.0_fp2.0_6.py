import lzma
lzmaobj=lzma.open(filename+".lzma","rb")
print(lzma.decompress(lzmaobj.read()))
lzmaobj.close()

print("\n\ndecompressing lzmafile with bz2")
import bz2
bz2obj=bz2.BZ2File(filename+".bz2","r")
print(bz2obj.read().decode("utf-8"))
bz2obj.close()

import zipfile
print("\n\ninflating zip file with zipfile")
zipobj=zipfile.ZipFile(filename+".zip","r")
filename2=zipobj.namelist()[0]
print(filename2)
print(zipobj.read(filename2).decode("ascii"))

print("\n\nusing gzip to write a different file")
import gzip
with gzip.open("anotherfile.gz","wt") as anotherfile:
	anotherfile.write("writing to a compressed file using gzip")

print("\n
