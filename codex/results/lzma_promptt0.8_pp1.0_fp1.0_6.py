import lzma
# Test LZMADecompressor
lzma_obj = lzma._decompressobj()
print(lzma_obj.decode(file_content))

# The result's length is 139152
print(len(lzma_obj.decode(file_content)))

# MemoryView ?
svn_file_content = lzma.decompress(file_content)
print(svn_file_content[68:70])

# Done
print("Done")
