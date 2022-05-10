from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#Prints the decompressed string
print(s.decode())


"""
Same as the code above but with the with statement
"""

with BZ2File('data/t20s.txt.bz2') as f:
    print(f.read().decode())

"""
The with statement is similar to try/finally
"""
try:
    f = open(path, 'w')
    f.write(foo)
finally:
    f.close()

with open(path, 'w') as f:
    f.write(foo)


"""
Example of a missing context manager. 
"""

f = open(path)


"""
Example using a custom context manager
"""

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
