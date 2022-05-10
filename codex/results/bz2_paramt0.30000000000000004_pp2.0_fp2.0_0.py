from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))

# The data is a tar file
import tarfile
tar = tarfile.open(fileobj=io.BytesIO(data))

# The tar file contains a file called data.bin
tar.extractall()

# The data.bin file is a gzip file
with gzip.open('data.bin', 'rb') as f:
    data = f.read()

# The data.bin file contains a file called data2.bin
with open('data2.bin', 'wb') as f:
    f.write(data)

# The data2.bin file is a zip file
with zipfile.ZipFile('data2.bin') as myzip:
    with myzip.open('data2.bin') as myfile:
        data = myfile.read()

# The data2.bin file contains a file called data3.bin
with open('data3.bin', 'wb') as f:
    f.write(data)

# The data3.bin file is a bzip2 file
with
