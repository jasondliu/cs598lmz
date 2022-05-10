import lzma
lzma.LZMAError

# Importing OK
print('lzma is OK')

# Testing
print('Testing .xz decompression...')

import subprocess
import os
import sys

# Get the directory
# os.path.dirname(sys.argv[0])
# os.path.realpath(__file__)
# os.path.abspath(__file__)
# os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
# os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), os.pardir))
# os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), os.pardir)), os.pardir))

#
