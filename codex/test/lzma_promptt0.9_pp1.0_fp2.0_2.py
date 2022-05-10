import lzma
# Test LZMADecompressor
#lzc = lzma.LZMADecompressor()

#result_string = lzc.decompress(f.read())

#with open('/tmp/result_string','wb') as r:
#    r.write(result_string)

#    r.close()
#    f.close()
# Indexing

# Track each "level" in the indexing file to fill the specific elements of the dict

tmp_name = list()
tmp_order = list()
tmp_first = list()
tmp_last = list()
tmp_length = list()
level = 0;
