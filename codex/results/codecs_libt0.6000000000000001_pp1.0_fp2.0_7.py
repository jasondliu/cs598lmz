import codecs
codecs.open('file.txt', 'r', encoding='utf-8')

# readline
f = open('file.txt', 'r')
f.readline()

# readlines
f = open('file.txt', 'r')
f.readlines()

# write
f = open('file.txt', 'w')
f.write('test')

# tell
f = open('file.txt', 'r')
f.tell()

# seek
f = open('file.txt', 'r')
f.seek(10)

# truncate
f = open('file.txt', 'w')
f.write('test')
f.truncate()

# close
f = open('file.txt', 'r')
f.close()

# with
with open('file.txt', 'r') as f:
    f.readline()

# filecmp
import filecmp
filecmp.cmp('file1.txt', 'file2.txt')

# os.walk
import os
rootdir = '.'
for root, subFolders
