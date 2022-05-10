import mmap
import sys
import os.path

ctr = 0

# file path

fname = 'woven.txt'

if not os.path.isfile(fname):
    print ("File path {} does not exist. Exiting".format(fname))
       
# open the file
fh = open(fname, 'r', newline='\r\n')

# use mmap to eliminate errors

mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)

if mm.readline()[:2] != b'\xff\xfe':
    print('Not a unicode file: {}'.format(fname))

# discard first three lines

mm.readline()
mm.readline()
