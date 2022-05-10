import mmap
# Test mmap.mmap()
import os
# Test os.truncate()
import random
# Test random.randint()
import subprocess
# Test subprocess.call()
import sys
# Test sys.version_info(), sys.exit(), sys.stdout.write()
import time
# Test time.time(), time.strftime(

try:
    import gmpy
    GMPY = 1
except:
    GMPY = 0

try:
    from Crypto.Hash import SHA256
    SHA256_EXT = 1
except:
    SHA256_EXT = 0

try:
    from Crypto.Cipher import AES
    AES_EXT = 1
except:
    AES_EXT = 0

try:
    from Crypto.Hash import SHA256
    SHA256_EXT = 1
except:
    SHA256_EXT = 0

