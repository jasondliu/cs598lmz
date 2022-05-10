import lzma
lzma.decompress(zipped_data)

# compress with zip
from zipfile import ZipFile
with ZipFile('compressed.zip', 'w') as f:
    f.write('example.txt')

# decompress with zip
from zipfile import ZipFile
with ZipFile('compressed.zip', 'r') as f:
    f.extractall()

# list zip contents
from zipfile import ZipFile
with ZipFile('compressed.zip') as f:
    print(f.namelist())

# compress with tar
import tarfile
with tarfile.open('compressed.tar', 'w') as f:
    f.add('example.txt')

# decompress with tar
import tarfile
with tarfile.open('compressed.tar', 'r') as f:
    f.extractall()

# list tar contents
import tarfile
with tarfile.open('compressed.tar') as f:
    print(f.getnames())
