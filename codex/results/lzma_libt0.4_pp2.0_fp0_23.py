import lzma
lzma.decompress(lzma.compress(b'\x00' * 1000000))

# $ time python3 -m timeit -s 'import lzma' 'lzma.decompress(lzma.compress(b"\x00" * 1000000))'
# 100 loops, best of 3: 2.5 msec per loop
# $ time python -m timeit -s 'import lzma' 'lzma.decompress(lzma.compress(b"\x00" * 1000000))'
# 100 loops, best of 3: 5.19 msec per loop

import zlib
zlib.decompress(zlib.compress(b'\x00' * 1000000))

# $ time python3 -m timeit -s 'import zlib' 'zlib.decompress(zlib.compress(b"\x00" * 1000000))'
# 1000 loops, best of 3: 1.08 msec per loop
# $ time python -m timeit -s 'import zlib' 'zlib.decompress(z
