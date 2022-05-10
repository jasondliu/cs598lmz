from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed).decode('utf-8')
</code>
Obs:. This solution doesn't work if your data was compressed using the file header. 
https://stackoverflow.com/a/51415953/9958987

