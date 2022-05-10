import bz2
bz2_file = bz2.BZ2File('data/data_sample.csv.bz2', 'w')
bz2_file.write(data_sample.to_csv().encode('utf-8'))
bz2_file.close()
 
!bzip2 -d -k data/data_sample.csv.bz2
!ls -ltr data/data_sample.csv

import bz2
bz2_file = bz2.BZ2File('data/data_sample.csv.bz2', 'r')
data_sample_decompressed = bz2_file.read()
bz2_file.close()

print(data_sample_decompressed.decode('utf-8'))
 
!rm data/data_sample.csv
!rm data/data_sample.csv.bz2

# Compression and Decompression with zlib
import zlib
data_sample_compressed = zlib.compress(data_sample.to_csv().encode('utf-8'))
print(data
