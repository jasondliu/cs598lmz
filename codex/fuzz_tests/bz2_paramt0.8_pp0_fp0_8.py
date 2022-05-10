from bz2 import BZ2Decompressor
BZ2Decompressor().decompress( bzipped )

#We have a zipfile. We read it with zipfile.
#The file is a list of id-passwords.
import zipfile
zipped = zipfile.ZipFile('channel.zip')
zipped.printdir()

#This is a comment: welcome to my zipped list.
print(zipped.read('readme.txt'))

#It says start from 90052, open the file and go again
next_file = '90052'
data = zipped.read(next_file+'.txt')
print(data)

while data.startswith('Next nothing is'):
    next_file = data.split()[-1]
    data = zipped.read(next_file+'.txt')
    print(next_file, data)

#This is not a file but a zipfile.
next_file = '90052'
data = zipped.read(next_file+'.txt')
print(data)
while data.startswith('Next nothing is'):
    next_file = data.split()
