import mmap
import math

header_files = ['/home/kaspars/projects/contamination/data/hdf5/cont_header.txt']

headers = []

for header_file in header_files:
    file_data = open(header_file, 'r')
    for line in file_data.readlines():
        l = line.split(',')
        headers.append(l)
    file_data.close()

headers = zip(*headers)

print headers

for seq in headers:
    print ' '.join(seq)


files = ['/home/kaspars/projects/contamination/data/hdf5/contamination_1.txt',
         '/home/kaspars/projects/contamination/data/hdf5/contamination_2.txt',
         '/home/kaspars/projects/contamination/data/hdf5/contamination_3.txt',
         '/home/kaspars/projects/contamination/data/hdf5/contamination_4.txt',
         '/home/kaspars/projects/contamination
