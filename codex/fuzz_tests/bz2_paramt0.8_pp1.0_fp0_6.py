from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bytearray(b))

# bz2.crc32(b'hello world')

import bz2
import sys
opener = bz2.open
if sys.platform.startswith('win'):
    import os, msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
for filename in sys.argv[1:]:
    with opener(filename, 'rt') as f:
        for line in f:
            sys.stdout.write(line)

# sys.stdout.write(line.encode('utf-8'))

import bz2
print([bz2.decompress(line.rstrip().encode('utf-8')).decode('utf-8')
       for line in open('./bzipped.bz2', 'rt')])

# output = subprocess.run(['grep', '-i', 'python'],
#                         input=open('ls.bz2', 'rb'),
#                        
