import bz2
bz2.BZ2File(path, 'rb')

# or

import bz2
bz2.open(path, 'rb')

# or

import bz2
with bz2.BZ2File(path, 'rb') as f:
    f.read()

# or

import bz2
with bz2.open(path, 'rb') as f:
    f.read()

# or

import bz2
f = bz2.BZ2File(path, 'rb')
try:
    f.read()
finally:
    f.close()

# or

import bz2
f = bz2.open(path, 'rb')
try:
    f.read()
finally:
    f.close()

# or

import bz2
with bz2.BZ2File(path, 'rb') as f:
    f.read()

# or

import bz2
with bz2.open(path, 'rb') as f:
    f.read
