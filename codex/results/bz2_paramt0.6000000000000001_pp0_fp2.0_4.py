from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#>>> import zlib
#>>> zlib.decompress(data)

#>>> import gzip
#>>> with gzip.open('file.gz', 'rb') as f:
#...     file_content = f.read()

import urllib.request
u = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')
#print(u.info())

import re

#r = re.compile('un: \'(.*)\', pw: (.*)')
r = re.compile('un: \'(\w+)\', pw: (\w+)')
content = str(u.read())
m = r.search(content)

import bz2
un = bz2.decompress(m.group(1).encode('utf-8')).decode('utf-8')
pw = bz2.decompress(m.group(2).encode('utf-8')).decode('utf-8')
print(un
