import bz2
bz2_file = bz2.BZ2File("file1.csv.bz2")
#print(bz2_file.read())
#bz2_file.close()

#4.4.4 gzip 压缩文件

import gzip
with gzip.open("file1.csv.gz",'rt') as gz_file:
    print(gz_file.read())
#gz_file.close()
