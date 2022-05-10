import bz2
bz2.BZ2File('C:\\Users\\Dell\\Desktop\\bz2_example.bz2')

# To open .gz file
import gzip
gzip.open('C:\\Users\\Dell\\Desktop\\gz_example.gz')

# To open .tar file
import tarfile
tar = tarfile.open('C:\\Users\\Dell\\Desktop\\tar_example.tar.gz')

# To open .zip file
import zipfile
zip = zipfile.open('C:\\Users\\Dell\\Desktop\\zip_example.zip')
'''

# To open .zip file
import zipfile
zip = zipfile.open('C:\\Users\\Dell\\Desktop\\zip_example.zip')

# To extract .zip file
with zipfile.ZipFile('C:\\Users\\Dell\\Desktop\\zip_example.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\\Users\\Dell\\Desktop\\')

# To extract .gz file
with gzip.open('C:\\Users\\D
