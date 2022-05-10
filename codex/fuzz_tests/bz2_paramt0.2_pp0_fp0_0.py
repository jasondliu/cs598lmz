from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bzip2 -d -c data.bz2 | wc -c
# bzip2 -d -c data.bz2 | tail -c 10
# bzip2 -d -c data.bz2 | tail -c 10 | od -c
# bzip2 -d -c data.bz2 | tail -c 10 | od -c | head -n 1

# bzip2 -d -c data.bz2 | tail -c 10 | od -c | head -n 1 | cut -d ' ' -f 2-

# bzip2 -d -c data.bz2 | tail -c 10 | od -c | head -n 1 | cut -d ' ' -f 2- | tr -d ' '

# bzip2 -d -c data.bz2 | tail -c 10 | od -c | head -n 1 | cut -d ' ' -f 2- | tr -d ' ' | tr -d '\n'

# bzip2 -d -c data.bz2 | tail -c 10 | od
