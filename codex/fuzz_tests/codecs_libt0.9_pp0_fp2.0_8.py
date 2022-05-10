import codecs
codecs.open("f:/hello.txt",'r','utf-8')
#=> <codecs.StreamReaderWriter at 0x2d7a550>

import os
os.chdir('f:/')
os.chdir('f:/hello.txt')
#Traceback (most recent call last):
#  File "<input>", line 1, in ?
#  File "D:\python24\lib\ntpath.py", line 203, in chdir
#    _chdir(path)
#OSError: [Errno 2] No such file or directory: 'f:/hello.txt'
#>>> 

os.chdir('f:/pyday3')
# >>> os.chdir('f:/pyday3')
# >>> os.getcwd()
# 'f:\\pyday3'

os.execv('l:\\mail\\office8\\explore.exe' ,['maple'])
#>>> 
#>>> 
#>>> os.closerange(20,25)
#>>> 
#>>> os.listdir('d:/')
#
