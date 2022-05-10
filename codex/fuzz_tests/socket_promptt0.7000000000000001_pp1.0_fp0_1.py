import socket
# Test socket.if_indextoname() using localhost interface index.
# expected output:
#   lo
socket.if_indextoname(1)

import ntpath
# Test ntpath.split() with a max_split argument.
# expected output:
#   ('C:\\', 'my.file')
ntpath.split('C:\\my.file', 1)

import shutil
# Test shutil.copyfileobj().
# expected output:
#   b'foobar\n'
with open('/dev/null', 'rb') as src, open('/dev/null', 'wb') as dst:
    shutil.copyfileobj(src, dst, 3)

import subprocess
# Test subprocess.Popen.communicate()
# expected output:
#   b'foo\n'
subprocess.Popen(['echo', 'foo'], stdout=subprocess.PIPE).communicate(timeout=0.1)

import sys
# Test sys.getsizeof().
# expected output:
#   874
sys.getsizeof(bytearray(
