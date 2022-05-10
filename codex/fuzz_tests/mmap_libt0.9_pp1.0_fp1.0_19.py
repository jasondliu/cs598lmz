import mmap 
import sys

file = sys.argv[1]
f = open(file, 'r')

print('The name of this script is {}'.format(sys.argv[0]))
print('The language interpreter is {}'.format(sys.executable))
print("Number of arguments:", len(sys.argv), 'arguments.')
print("Argument values:", str(sys.argv))

f = open(file)
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('\x50\x4b\x03\x04') != -1:
    print('This zip file is not password protected!')
else:
    print('This zip file is password protected.\nConsider the following names:admin,pass,password,winrar,etc...')

##########
if len(sys.argv) != 1:
    sys.exit("Usage : python script.py <zip_file>")

from zipfile import ZipFile
import itertools

zip_file =
