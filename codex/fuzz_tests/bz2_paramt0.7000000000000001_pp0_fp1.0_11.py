from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(doc)

import tarfile
t = tarfile.open('apache-tomcat-8.5.5.tar.gz')
t.extractall()
t.close()

import zipfile
z = zipfile.ZipFile('test.zip', 'w')
z.write('test1.txt')
z.write('test2.txt')
z.close()

z = zipfile.ZipFile('test.zip', 'r')
z.extractall('test')
z.close()

import this
