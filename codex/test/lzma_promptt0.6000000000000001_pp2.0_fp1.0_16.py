import lzma
# Test LZMADecompressor by decompressing the LZMA-compressed data created above.
# This requires the Python lzma module (available from http://www.sf.net/projects/pyliblzma).

try:
    from lzma import LZMADecompressor
except ImportError:
    import sys
    print(sys.exc_info()[1])
    print('Skipping LZMADecompressor tests')
else:
    print('Testing LZMADecompressor')
