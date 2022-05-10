from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Error -3 while decompressing data: invalid distance code
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "D:\GitHub\Python\Python-100-Days\Day01-15\08. 字符串、列表、元组、字典、集合\lzma_demo.py", line 9, in <module>
#     LZMADecompressor().decompress(data)
#   File "D:\GitHub\Python\Python-100-Days\venv\lib\site-packages\lzma\lzma.py", line 288, in decompress
#     return self.decompress(input, max_length, True)
#   File "D:\GitHub\Python\Python-100-Days\venv\lib\site-packages\lzma\lzma.py", line 277, in decompress
#    
