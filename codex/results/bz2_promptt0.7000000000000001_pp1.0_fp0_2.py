import bz2
# Test BZ2Decompressor
#import bz2
#with open('/home/lucas/Downloads/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
#    decompressor = bz2.BZ2Decompressor()
#    for block in iter(lambda : f.read(100 * 1024), ''):
#        print(len(decompressor.decompress(block)))
#    print(len(decompressor.decompress()))

#from bz2file import BZ2File
#bz = BZ2File('/home/lucas/Downloads/enwiki-latest-pages-articles.xml.bz2')
#for line in bz:
#    print(line)
#    break

from xml.etree.ElementTree import iterparse

import json 
def generate_titles():
    with bz2.open('/home/lucas/Downloads/enwiki-latest-pages-articles.xml.bz2') as f:
        for _, element in iterparse(f, events=('
