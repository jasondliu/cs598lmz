import bz2
bz2_data = bz2.compress(data)
print(bz2_data)
print('Compressed size is: %f'%(len(bz2_data)))

print('Compressed by %f'%(len(data)/len(bz2_data)))

orig_data = bz2.decompress(bz2_data)
print(orig_data)

pickle_data = pickle.dumps(data)
print(pickle_data)
print('Compressed size is: %f'%(len(pickle_data)))

print('Compressed by %f'%(len(data)/len(pickle_data)))

orig_data = pickle.loads(pickle_data)
print(orig_data)

import gzip
gzip_file = gzip.open('gzip_data', 'wb')
gzip_file.write(data)
gzip_file.close()

import shutil
with open('data', 'rb') as input:
    with gzip.open('gzip_data', '
