import bz2
bz2.decompress(data)

#bz2 module
import bz2
bz2.compress(data)

#tarfile
import tarfile
tar = tarfile.open("sample.tar.bz2", "w:bz2")
for name in ["foo.txt", "bar.txt", "spam.txt", "eggs.txt"]:
    tar.add(name)
tar.close()

tar = tarfile.open("sample.tar.bz2", "r:bz2")
tar.extractall(path="tmp")
tar.close()

#gzip
import gzip
f = gzip.open('file.txt.gz', 'rb')
file_content = f.read()
f.close()

f = gzip.open('file.txt.gz', 'wb')
f.write(file_content)
f.close()

#zipfile
import zipfile
zf = zipfile.ZipFile("sample.zip", "w", zipfile.ZIP_DEFLATED)
zf.write("
