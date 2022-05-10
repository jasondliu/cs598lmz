import lzma
lzma.LZMAFile(open('/home/ubuntu/inputs/input_file.csv')).read()

# Decompress
import lzma
lzma.LZMAFile(open('/home/ubuntu/inputs/input_file.csv.xz')).read()

# Compress
import bz2
bz2.BZ2File('/home/ubuntu/inputs/input_file.csv').read()

# Decompress
import bz2
bz2.BZ2File('/home/ubuntu/inputs/input_file.csv.bz2').read()

# Compress
import zipfile
zipfile.ZipFile('/home/ubuntu/inputs/input_file.csv').read()

# Decompress
import zipfile
zipfile.ZipFile('/home/ubuntu/inputs/input_file.csv.zip').read()

# Compress
import gzip
gzip.GzipFile('/home/ubuntu/inputs/input_file.csv').read()

# Decompress
import g
