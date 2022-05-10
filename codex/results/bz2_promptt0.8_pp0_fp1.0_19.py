import bz2
# Test BZ2Decompressor

stdin = """BZh9"""

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(stdin)

with open("xmen.xml.bz2") as in_file:
    file_content = in_file.read()

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(file_content)

# 
# It's working
# 
# decompressor.decompress(file_content)
# XML ASCII text
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


# with open("xmen.xml.bz2") as in_file:
#     file_content = in_file.read()
# 
# 
# 
# decompressor = bz2.BZ2Decompressor()
# 
# decompressor.decompress(stdin)
# 
# decompressor.flush()
# 

