from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(response.content)

#overview = response.content[:overview_length]
#print(overview)
