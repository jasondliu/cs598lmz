import mmap
import hashlib
import os

# This script will take a file and a byte offset, and give you the md5sum of the first chunk

usage = "Usage: %prog [options] -f FILE -o OFFSET"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", help="File to be analyzed")
parser.add_option("-o", "--offset", help="Offset to start chunking")

(options, args) = parser.parse_args()
filename = options.file
offset = int(options.offset)

# Check to see if file is valid
if not os.path.exists(filename):
    print "File does not exist"
    exit(0)

with open(filename) as f:
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

subset = data[offset:offset+524288]
md5 = hashlib.md5()
md5.update(subset)
print md5.hexdigest()
