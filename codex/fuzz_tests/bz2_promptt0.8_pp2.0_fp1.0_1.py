import bz2
# Test BZ2Decompressor in conjunction with GzipFile
# and FileIO
from bz2file import BZ2File
from io import BufferedReader, BytesIO
from test.support import run_unittest, captured_stdout

filename = test_support.findfile("gzip_test.txt")
filename2 = test_support.findfile("gzip_test2.txt")

# Test data is a 12-byte file
# The compressed data was created with:
# bin/gzip -c foo | bin/bzip2 -c > foo.bz2

compressed =  b'BZh91AY%\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x19' \
             + b'%\x83P\x00\x00\x00\x00\xc9\x10\x0c\x00\x00\x00\x00\x00\x00\x00\x00' \
             + b'\x00\x00\x00\x
