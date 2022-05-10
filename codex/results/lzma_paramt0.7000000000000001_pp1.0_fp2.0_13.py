from lzma import LZMADecompressor
LZMADecompressor().decompress(zlib.decompress(open(sys.argv[1], 'rb').read()))

# Uncompressed binary:
#
# ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=f077e0e9b290c7d2f0cd8c2d2d57bafc709258e1, stripped
#
#
# 0x00000000004006d0 <+0>:     mov    rax,0xc40404040404040404040404
# 0x00000000004006da <+10>:    mov    rdx,rax
# 0x00000000004006dd <+13>:    mov    rax,rdx
# 0x00000000004006e0 <+16>:    shr    rax,0x3f
# 0x00000000004006e4 <+20>:    xor    rax,rdx
# 0x0000000000400
