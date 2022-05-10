import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(bz2_data)
# Test BZ2File
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()

# Test GzipFile
import gzip
gzip_file = gzip.GzipFile('example.gz')
gzip_file.read()

# Test ZipFile
import zipfile
zip_file = zipfile.ZipFile('example.zip')
zip_file.namelist()
zip_file.getinfo('README.txt')
zip_file.read('README.txt')

# Test tarfile
import tarfile
tar_file = tarfile.open('example.tar.gz')
tar_file.getnames()
tar_file.extractall()
tar_file.close()

# Test pickle
import pickle
pickled_string = pickle.dumps([1, 2, 3, 'a', 'b', 'c'])
pickle.loads
