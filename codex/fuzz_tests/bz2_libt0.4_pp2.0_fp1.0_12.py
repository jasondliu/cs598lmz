import bz2
bz2_file = bz2.BZ2File("sample.bz2")
data = bz2_file.read()
print(data)

# GZIP
import gzip
gzip_file = gzip.open("sample.gz", "rb")
data = gzip_file.read()
print(data)

# ZIP
import zipfile
zip_file = zipfile.ZipFile("sample.zip")
print(zip_file.namelist())

# TAR
import tarfile
tar_file = tarfile.open("sample.tar.gz")
print(tar_file.getnames())

# COMPRESSED FILE
import shutil
with open("sample.txt", "rb") as f_in:
    with gzip.open("sample.txt.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open("sample.txt.gz", "rb") as f_in:
    with open("sample.txt", "wb") as f_out:
        shutil.
