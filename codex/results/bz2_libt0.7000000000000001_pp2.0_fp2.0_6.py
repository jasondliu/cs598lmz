import bz2
bz2.decompress(bz2.compress(b'hello world!'))

import zipfile
with zipfile.ZipFile('test_zip.zip','w') as myzip:
    myzip.write('test_zip.txt')
    myzip.write('test_zip.csv')
    myzip.write('test_zip.py')


 
import zipfile
with zipfile.ZipFile('test_zip.zip','r') as myzip:
    myzip.extractall('../temp_dir')
    
    
    
    
    
#直接用import即可
import os,sys
print(os.path.abspath('.'))
print(os.path.join('/home/peter/temp', 'testdir'))
current_dir=os.path.join('/home/peter/temp', 'testdir')
os.mkdir(current_dir)
os.rmdir(current_dir)

print(os.path.splitext('/home/peter/temp/testdir/test
