import bz2
bz2.BZ2File

with open('', 'rb') as f:
    file_content = f.read()

with bz2.BZ2File('', 'w') as f:
    f.write(file_content)

# tar.gz
import tarfile
import os

with tarfile.open('', 'w:gz') as tr:
    tr.add('', arcname=os.path.basename(''))

# tar.bz2
with tarfile.open('', 'w:bz2') as tr:
    tr.add('', arcname=os.path.basename(''))
    
# tar.xz unzip
with tarfile.open('', 'r:xz') as tr:
    tr.extractall()
    
# tar.xz zip
import tarfile
import os

with tarfile.open('', 'w:xz') as tr:
    tr.add('', arcname=os.path.basename(''))

# tar.zip unzip
import zipfile

with zipfile
