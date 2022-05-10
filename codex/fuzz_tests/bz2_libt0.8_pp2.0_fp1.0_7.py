import bz2
bz2.decompress(data)

# bz2 - python3
with bz2.BZ2File('file.bz2', 'r') as f:
    file_content = f.read()

# gzip - python3
with gzip.open('file.gz', 'rt') as f:
    file_content = f.read()

# zip
with zipfile.ZipFile('file.zip', 'r') as zip_ref:
    zip_ref.extractall('extract_path')

import tarfile
tar = tarfile.open('file.tar')
tar.extractall('extract_path')
tar.close()

# tar.gz - python3
with tarfile.open('file.tar.gz', 'r:gz') as tar:
    tar.extractall('extract_path')
