import bz2
bz2_file = bz2.BZ2File('file.bz2')
file_content = bz2_file.read()
bz2_file.close()

# gzip 
import gzip
import shutil
gzip_file = gzip.open('file.gz', 'rb')
file_content = gzip_file.read()
gzip_file.close()

# tar
import tarfile
tar = tarfile.open("sample.tar.gz", "r:gz")
tar.extractall()
tar.close()

# zip
import zipfile
zip_file = zipfile.ZipFile('file.zip', 'r')
for name in zip_file.namelist():
	zip_file.extract(name, 'temp/')
zip_file.close()

# pickle
# serialize object to a file
import pickle
pickle.dump(obj, file, [,protocol])
# read object from a file
obj = pickle.load(file)

# shelve
import shelve

s = shelve.
