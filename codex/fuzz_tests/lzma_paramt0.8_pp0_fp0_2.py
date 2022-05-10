from lzma import LZMADecompressor
LZMADecompressor().decompress(p)

# %%
from zlib import decompress
decompress(p)

# %%
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(p)


a = p1
while a[-2:] != b'\x90\x00':
    a = decompress(a)
print(a)

# %%
from pwn import *
r = remote('chall.pwnable.tw', 10100)
r.send(p1)

# %%
from pwn import *
r = remote('chall.pwnable.tw', 10100)
r.send(p1)

# %%
a = p1
while a[-2:] != b'\x90\x00':
    a = decompress(a)
print(a)

# %%
a = p1
while a[-2:] != b'\x90\x00':
    a = decompress(a)
print(a)

# %%
from pwn import *
r = remote('chall
