import bz2
bz2.decompress(zipped)

bz2.compress(unzipped)

# Using zlib
import zlib
zipped = zlib.compress(unzipped)
zlib.decompress(zipped)



# Gzip
import gzip
f = gzip.open('somefile.gz', 'rb')
file_content = f.read()
f.close()

import gzip
f_out = gzip.open('somefile.gz', 'wb')
f_out.write(file_content)
f_out.close()

# Bzip2
import bz2
f = bz2.BZ2File('somefile.bz2', 'rb')
file_content = f.read()
f.close()

import bz2
f_out = bz2.BZ2File('somefile.bz2', 'wb')
f_out.write(file_content)
f_out.close()

# Zip
import zipfile
f = zipfile.ZipFile('somefile.zip', '
