from lzma import LZMADecompressor
LZMADecompressor.decompress(b"\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# issue.py

#!/usr/bin/env python3
import lzma
import sys

if __name__ == '__main__':
    lzma.decompress(sys.stdin.buffer.read())

# test.sh

#!/usr/bin/env bash

python3 issue.py < input.xz > /dev/null

# input.xz

#!/usr/bin/env bash

xz -9e input.txt

# input.txt

#!/usr/bin/env bash

cat /dev/zero | head -c 100000000 > input.txt

# issue.py

#!/usr/bin/env python3
import lzma
import sys

if __name__ == '
