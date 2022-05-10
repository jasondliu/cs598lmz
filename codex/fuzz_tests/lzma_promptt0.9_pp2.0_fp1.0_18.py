import lzma
# Test LZMADecompressor
uncompr_wrd_lrn = cPickle.dumps(wrd_lrn)
lzcpr=lzma.LZMADecompressor()
cprsd=lzcpr.compress(uncompr_wrd_lrn)
ucprsd=lzcpr.decompress(cprsd)
print(type(uncompr_wrd_lrn),len(uncompr_wrd_lrn),type(cprsd),len(cprsd),type(ucprsd),len(ucprsd))
# Results [no compression]
# <type 'str'> 57633 <type 'str'> 57988 <type 'str'> 57988

# Test LZMACompressor
cmp=lzma.LZMACompressor()
cprsd=cmp.compress(uncompr_wrd_lrn)
ucprsd=cmp.flush()
print(type(uncompr_wrd_lrn),len(uncompr_wrd_lrn),type(cprsd),len(cprsd
