import bz2
bz2_file = bz2.BZ2File('data/sample.csv.bz2')
file_content = bz2_file.read()
bz2_file.close()

# Read from a gzip file
import gzip
gzip_file = gzip.open('data/sample.csv.gz', 'rb')
file_content = gzip_file.read()
gzip_file.close()

# Read from a zip file
from zipfile import ZipFile
zf = ZipFile('data/sample.zip')
file_name = zf.namelist()[0]
file_content = zf.read(file_name)
zf.close()

# Read from a tar file
from tarfile import TarFile
tar = TarFile('data/sample.tar')
file_name = tar.getnames()[0]
file_content = tar.extractfile(file_name).read()
tar.close()

# Read from a tar.gz file
from tarfile import TarFile
tar_gz = TarFile('data/sample.tar.gz
