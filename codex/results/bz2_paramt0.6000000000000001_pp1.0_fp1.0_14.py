from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('channel.zip.bz2','rb').read())

# with open('channel.zip','wb') as f:
#     f.write(bz2.decompress(open('channel.zip.bz2','rb').read()))

# with ZipFile('channel.zip') as myzip:
#     myzip.extractall()
#     print(myzip.namelist())

# content = open('channel/readme.txt','r').read()
# print(content)

import re

#next_nothing=90052
#next_nothing=94191
next_nothing='46145'

# for i in range(1000):
#     content = open('channel/'+next_nothing+'.txt','r').read()
#     next_nothing = re.findall(r'Next nothing is (\d+)',content)[0]
#     print(content)

# with ZipFile('channel.zip') as myzip:
#     for i in range(1000):
#         content = myzip.read('{}.
