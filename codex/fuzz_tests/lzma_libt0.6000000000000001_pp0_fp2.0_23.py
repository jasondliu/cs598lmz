import lzma
lzma.decompress

# uncompress a file
# https://stackoverflow.com/questions/3126409/how-to-uncompress-a-file-with-python
import gzip
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()

# https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
import gzip
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()

# https://stackoverflow.com/questions/3126409/how-to-uncompress-a-file-with-python
import bz2
with bz2.BZ2File('file.txt.bz2', 'rb') as f:
    file_content = f.read()

# https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
import bz2

