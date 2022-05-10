import lzma
lzma.open

# OK
import lzma
lzma.LZMAFile

# OK
import lzma
lzma.LZMAFile(mode='r')

# OK
import lzma
print(lzma.LZMAFile)

# OK
import lzma
print(lzma.open)

# OK
import lzma
lzma.LZMAFile(mode='r').__class__

# OK
import lzma
lzma.LZMAFile(mode='r').__class__()


import sys
sys.stdin.read

# OK
import sys
sys.stdin.__class__

# OK
import sys
sys.stdin.__class__.read

# OK
import sys
sys.stdin.__class__().read


import sys
sys.stdout.write

# OK
import sys
sys.stdout.__class__

# OK
import sys
sys.stdout.__class__.write

# OK
import sys
sys.std
