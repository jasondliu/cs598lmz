import mmap
import struct
import sys
import re

#Some useful info
#Struct format characters: http://docs.python.org/library/struct.html
#                        H: unsigned short
#                        h: signed short
#                        I: unsigned int
#                        i: signed int
#                        q: long long
#                        d: double
#See the unpack function here: http://docs.python.org/library/struct.html#struct.unpack
#See file.seek here: http://docs.python.org/library/stdtypes.html?highlight=seek#file.seek

class IndexedFasta:
    def __init__(self,fasta,index):
        self.mapfile=mmap.mmap(open(fasta).fileno(),0,access=mmap.ACCESS_READ)
        self.index=open(index,"rb") #use binary reading because we need to extract numbers
        self.offset=0
        
    def check(self):
        try:
            print self.mapfile[0:100]
            print self.mapfile[0:100].count
