import mmap
# Test mmap.mmap Can Read Content from a File
import sys,os,io
datapath = 'C:\\Users\\zhou\\Downloads\\'
filenam = 'dssp_all.txt'

fp = open(datapath+filenam)

fp.seek(0, 2)
fsize = fp.tell()
fp.seek(0)

readt = mmap.PROT_READ

if sys.version_info.major == 2:
    fpm = mmap.mmap(fp.fileno(),fsize, access = readt)
elif sys.version_info.major == 3:
    import mmap
    fpm = mmap.mmap(fp.fileno(),fsize, access = readt).read().decode('utf-8')
else:
    print('Unknown Python version')
    sys.exit()

print (fpm[:100])

print ('\nDone\n')

fp.close()


import re,os
# Test mmap.mmap Can be Used as a File-Like Object
print ('Test mm
