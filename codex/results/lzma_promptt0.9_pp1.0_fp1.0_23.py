import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
with open("xz/python3.xz", "rb") as f:
    compressed = f.read()
# Decompress
decompressed = decomp.decompress(compressed)
# Check if it's still the same (it should be)
assert(decompressed == compressed)
# Get the original file (from MSoft, lets hope its authentic)
import urllib.request
urllib.request.urlretrieve("https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe", "orig_python.exe")

# Get the xz archived version of the file
import lzma
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
# Reading the encrypted python executable
with open("xz/python.xz","rb") as
