import bz2
bz2.open()
'''

import bz2

with bz2.open('file.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.open('file.bz2', 'r') as f:
    print(f.read())

'''
import bz2
bz2.open()
'''

import bz2

with bz2.open('file.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.open('file.bz2', 'rb') as f:
    print(f.read())

'''
import bz2
bz2.open()
'''

import bz2

with bz2.open('file.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

'''
import b
