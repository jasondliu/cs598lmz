import lzma
lzma.decompress  # <built-in function decompress>

# https://docs.python.org/3.7/library/lzma.html
# https://python-lzma.readthedocs.io/en/latest/

# lzma is a built-in module in Python 3.3 and later.
# For earlier Python versions, use the backported lzma module from PyPI.

# $ python3.6 -m lzma -d 
# lzma module is not available

# pip install lzma

# $ python3.6 -m lzma -d 
# lzma module is not available

# pip install pylzma

# $ python3.6 -m lzma -d 
# lzma module is not available

# The pylzma module is a Python wrapper for the liblzma C library.
# The module contains a single class, LZMAFile, which is a PEP-3151 file-like object that can be used the same way as any other Python file object.

#
