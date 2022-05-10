from lzma import LZMADecompressor
LZMADecompressor()
 
# usage
c = LZMADecompressor()
chunk = c.decompress(data)

# memory & cpu intensive
# please use py7zip (python-p7zip) instead
# or use the precompiled lzma sdk in windows
