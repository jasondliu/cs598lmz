import bz2
# Test BZ2Decompressor
with open('test.bzip2', 'rb') as f_in, \
     open('test.txt', 'wb') as f_out:
  data = f_in.read()
  BZ2Decompressor().process_data(data, f_out)

import bz2
with open('test.bzip2', 'rb') as f1, \
     open('test.bzip2', 'rb') as f2, \
     open('test.bzip2', 'rb') as f3, \
     open('test.bzip2', 'rb') as f4:
    f1.read(10), f2.read(10), f3.read(10), f4.read(10)


import bz2
with open('test.bzip2.bk', 'rb') as f1, \
     open('test.bzip2.bk', 'rb') as f2, \
     open('test.bzip2.bk', 'rb') as f3, \
     open('test.bzip2.bk', 'rb')
