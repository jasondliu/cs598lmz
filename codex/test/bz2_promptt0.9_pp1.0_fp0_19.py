import bz2
# Test BZ2Decompressor with incomplete input
in_text = bz2.compress(b'repeat me!')
for x in range(5):
    dec = bz2.BZ2Decompressor()
    try:
        dec.decompress(in_text[:x])
    except EOFError as e:
        print("{}: {}".format(x, e))



# BZ2 Compress files
"""
>>> import bz2
>>> f = bz2.open("data.bz2")
>>> text = f.read()
>>> f.close()
"""
# We can also use 'with' statement to make the process implicit.
'''
>>> with bz2.open("data.bz2") as f:
...     text = f.read()
...

'''
