import lzma
# Test LZMADecompressor

# Test that LZMADecompressor can decompress a simple LZMA stream.

# The stream was compressed with xz --format=lzma --check=crc32
# --lzma1=dict=128KiB,lc=3,lp=0,pb=2,mode=normal,nice=273,mf=bt4,depth=0
# --stdout --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose --verbose --verbose --verbose --verbose
# --verbose --verbose
