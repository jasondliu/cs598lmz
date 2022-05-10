from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# %%
import sys
sys.stdout.buffer.write(b'Hello\n')

# %%
sys.stdout.write('Hello\n')

# %%
sys.stdout.buffer.write(b'Hello\xe2\x98\x83\n')

# %%
sys.stdout.write('Hello\u2603\n')

# %%
sys.stdout.buffer.write(b'Hello\xe2\x98\x83\n')

# %%
sys.stdout.write('Hello\u2603\n')

# %%
sys.stdout.buffer.write(b'Hello\xe2\x98\x83\n')

# %%
sys.stdout.write('Hello\u2603\n')


