import bz2
bz2.open('data/file.bz2')
import bz2
with open('data/file.bz2') as f:
    f_bz2 = bz2.BZ2File(f)
    print(f_bz2.readline())
import bz2
f_bz2 = bz2.open('data/file.bz2', mode='wt')
f_bz2.write('Hello, world!')
f_bz2.close()
with bz2.open('data/file.bz2', mode='wt') as f:
    f.write('Hello, world!')

 
import bz2
with open('data/file.bz2', 'wt') as f, bz2.open(f, mode='wt') as f_out:
    f_out.write('Hello, world!')

import bz2
bz2.open('data/file.bz2', 'r')
import bz2
f = bz2.BZ2File('data/file.bz2')

