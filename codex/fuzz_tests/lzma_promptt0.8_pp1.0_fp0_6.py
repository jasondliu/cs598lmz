import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(b"\x00\x00\x00\x03\x00")

# Test LZMACompressor
comp = lzma.LZMACompressor()
comp.compress(b"foo")
comp.flush()


import runpy
runpy.run_module("lzma")
runpy.run_module("lzma", run_name="__main__")


import pickle
import types

code = """
def f(x):
    x += 2
    return x
"""

d = {}
exec(code, d, d)

pickle.loads(pickle.dumps(d["f"]))


import pickle
import types

def f(x):
    x += 2
    return x

pickle.loads(pickle.dumps(f))



import pickle

pickle.loads(b"c__main__\nfoo\np0\n.")


import pickle

# XXX: The
