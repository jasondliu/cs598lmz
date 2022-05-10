from lzma import LZMADecompressor
LZMADecompressor().decompress(tweet)

# This kind of error handling is exactly why we should use try/except/finally.

class LZMAError(Exception):
    pass

def pylzma(data):
    try:
        return LZMADecompressor().decompress(tweet)
    except lzma.LZMAError:
        raise LZMAError("couldn't decompress the data") from None
    finally:
        LZMADecompressor().flush()

# For example, now we can use the following code to try decompressing two tweets:

for tweet in tweets:
    try:
        print(pylzma(tweet))
    except LZMAError as err:
        print("Error:", err)

# which is nice.

# contextlib always provides the context manager protocol to generator
# functions. Here's what that means and what it looks like:

def upper_context(filename):
    with open(filename) as fin:
        for linenum, line in enumerate(fin, start=1):
            yield
