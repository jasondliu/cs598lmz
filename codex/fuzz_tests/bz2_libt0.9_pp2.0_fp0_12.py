import bz2
bz2.open()
'''


import tarfile

file = tarfile.TarFile('../files/test2.tar.gz', 'r')

print file.getnames()

help(tarfile.TarFile)

'''
for filein in file.getnames():
  print file.extractfile(filein).read()
'''

import os
os.system('chmod 777 test2.tar.gz')

file2 = tarfile.TarFile('../files/test2.tar.gz', 'w:gz')

help(file2)

os.stat('../files/test1.txt')

os.utime('../files/test1.txt', None)
file2.add('../files/test1.txt')
file2.close()

print
print
file3 = tarfile.TarFile('../files/test3.tar.gz', 'w:gz')

help(file3)

file3.add('../files/test1.txt', arcname='testarcfile.txt')

for member_info in file
