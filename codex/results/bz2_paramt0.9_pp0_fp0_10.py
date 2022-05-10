from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(lines[-1])

# Using the documentation in the Bzip 2 documentation
# https://docs.python.org/2/library/bz2.html
#Start: (SNIP 9)
#End  : (SNIP 10)
lines = open('un-commons-hosts.txt.bz2').readlines()
lines

#Start: (SNIP 11)
#End  : (SNIP 12)
unpacked_data = b''.join(lines[:-1]) + lines[-1][:-1]

#Start: (SNIP 13)
#End  : (SNIP 14)
raw_text = BZ2Decompressor().decompress(unpacked_data).decode('utf-8')
len(raw_text)

#Start: (SNIP 15)
#End  : (SNIP 16)
unique_words = set(raw_text.split())
unique_words

#Start: (SNIP 17)
#End  : (SNIP 18)
import bz2
 
data = b'BZh91
