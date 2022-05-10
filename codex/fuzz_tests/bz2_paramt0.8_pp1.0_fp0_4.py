from bz2 import BZ2Decompressor
BZ2Decompressor()
from tarfile import TarFile
from io import BytesIO
bytes_data = BytesIO(data_compressed)
 
bz_decompressor = BZ2Decompressor()
 
tarfile_data = TarFile(fileobj=bytes_data)
tarfile_data.extractall(path='./')

# Get list of files from 'file_name'
Files = [f for f in listdir(path) if isfile(join(path, f))]

# check if the file is present
if file_name in Files:
    print('File is present in the directory')
else:
    print('File is not present in the directory')

# Get the total number of files
print('Total Number of files in path {}'.format(len(Files)))
print(len(Files))

# Get list of images present in 'notMNIST_large/A'
Images = [f for f in listdir(path) if isfile(join(path, f)) & (f.endswith('.png'))]
print('Total number of images in path {}
